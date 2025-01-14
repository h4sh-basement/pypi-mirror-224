/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function () {
    'use strict';

    angular
        .module('refstackApp')
        .controller('GuidelinesController', GuidelinesController);

    GuidelinesController.$inject =
        ['$filter', '$http', '$uibModal', 'refstackApiUrl'];

    /**
     * RefStack Guidelines Controller
     * This controller is for the '/guidelines' page where a user can browse
     * through tests belonging to Interop WG defined capabilities.
     */
    function GuidelinesController($filter ,$http, $uibModal, refstackApiUrl) {
        var ctrl = this;

        ctrl.getVersionList = getVersionList;
        ctrl.update = update;
        ctrl.updateTargetCapabilities = updateTargetCapabilities;
        ctrl.filterStatus = filterStatus;
        ctrl.getObjectLength = getObjectLength;
        ctrl.openTestListModal = openTestListModal;
        ctrl.updateVersionList = updateVersionList;
        ctrl.gl_type = 'powered';

        /** The target OpenStack marketing program to show capabilities for. */
        ctrl.target = 'platform';

        /** The various possible capability statuses. */
        ctrl.status = {
            required: true,
            advisory: false,
            deprecated: false,
            removed: false
        };

        /**
         * The template to load for displaying capability details.
         */
        ctrl.detailsTemplate = 'components/guidelines/partials/' +
                               'guidelineDetails.html';

        /**
        * Update the array of dictionary objects which stores data
        * pertaining to each guideline, sorting them in descending
        * order by guideline name. After these are sorted, the
        * function to update the capabilities is called.
        */
        function updateVersionList() {
            let gl_files = ctrl.guidelineData[ctrl.gl_type];
            ctrl.versionList = $filter('orderBy')(gl_files, 'name', true);
            // Default to the first approved guideline which is expected
            // to be at index 1.
            ctrl.version = ctrl.versionList[1];
            update();
        }

        /**
         * Retrieve a dictionary object comprised of available guideline types
         * and and an array of dictionary objects containing file info about
         * each guideline file pertaining to that particular guideline type.
         * After a successful API call, the function to sort and update the
         * version list is called.
        */
        function getVersionList() {
            var content_url = refstackApiUrl + '/guidelines';
            ctrl.versionsRequest =
                $http.get(content_url).success(function (data) {
                    ctrl.guidelineData = data;
                    updateVersionList();
                }).error(function (error) {
                    ctrl.showError = true;
                    ctrl.error = 'Error retrieving version list: ' +
                        angular.toJson(error);
                });
        }

        /**
         * This will contact the Refstack API server to retrieve the JSON
         * content of the guideline file corresponding to the selected
         * version.
         */
        function update() {
            ctrl.content_url = refstackApiUrl + '/guidelines/'
                + ctrl.version.file;
            let get_params = {'gl_file': ctrl.version.file};
            ctrl.capsRequest =
                $http.get(ctrl.content_url, get_params).success(
                function (data) {
                    ctrl.guidelines = data;
                    if ('metadata' in data && data.metadata.schema >= '2.0') {
                        ctrl.schema = data.metadata.schema;
                        ctrl.criteria = data.metadata.scoring.criteria;
                        ctrl.releases =
                            data.metadata.os_trademark_approval.releases;
                        ctrl.guidelineStatus =
                            data.metadata.os_trademark_approval.status;
                    } else {
                        ctrl.schema = data.schema;
                        ctrl.criteria = data.criteria;
                        ctrl.releases = data.releases;
                        ctrl.guidelineStatus = data.status;
                    }
                    ctrl.updateTargetCapabilities();

                }).error(function (error) {
                    ctrl.showError = true;
                    ctrl.guidelines = null;
                    ctrl.error = 'Error retrieving guideline content: ' +
                        angular.toJson(error);
                });
        }

        /**
         * This will update the scope's 'targetCapabilities' object with
         * capabilities belonging to the selected OpenStack marketing program
         * (programs typically correspond to 'components' in the Interop WG
         * schema). Each capability will have its status mapped to it.
         */
        function updateTargetCapabilities() {
            ctrl.targetCapabilities = {};
            var components = ctrl.guidelines.components;
            var targetCaps = ctrl.targetCapabilities;
            var targetComponents = null;

            var old_type = ctrl.gl_type;
            if (ctrl.target === 'dns' ||
                ctrl.target === 'orchestration' ||
                ctrl.target === 'shared_file_system' ||
                ctrl.target === 'load_balancer' ||
                ctrl.target === 'key_manager'
               ) {
                ctrl.gl_type = ctrl.target;
            } else {
                ctrl.gl_type = 'powered';
            }
            // If it has not been updated since the last program type change,
            // will need to update the list
            if (old_type !== ctrl.gl_type) {
                updateVersionList();
                return;
            }

            // The 'platform' target is comprised of multiple components, so
            // we need to get the capabilities belonging to each of its
            // components.
            if (ctrl.target === 'platform' || ctrl.schema >= '2.0') {
                if ('add-ons' in ctrl.guidelines) {
                    targetComponents = ['os_powered_' + ctrl.target];
                } else if (ctrl.schema >= '2.0') {
                    var platformsMap = {
                        'platform': 'OpenStack Powered Platform',
                        'compute': 'OpenStack Powered Compute',
                        'object': 'OpenStack Powered Storage'
                    };

                    targetComponents = ctrl.guidelines.platforms[
                        platformsMap[ctrl.target]].components.map(
                            function(c) {
                                return c.name;
                            }
                        );
                } else {
                    targetComponents = ctrl.guidelines.platform.required;
                }

                // This will contain status priority values, where lower
                // values mean higher priorities.
                var statusMap = {
                    required: 1,
                    advisory: 2,
                    deprecated: 3,
                    removed: 4
                };

                // For each component required for the platform program.
                angular.forEach(targetComponents, function (component) {
                    // Get each capability list belonging to each status.
                    var componentList = components[component];
                    if (ctrl.schema >= '2.0') {
                        componentList = componentList.capabilities;
                    }
                    angular.forEach(componentList,
                        function (caps, status) {
                            // For each capability.
                            angular.forEach(caps, function(cap) {
                                // If the capability has already been added.
                                if (cap in targetCaps) {
                                    // If the status priority value is less
                                    // than the saved priority value, update
                                    // the value.
                                    if (statusMap[status] <
                                        statusMap[targetCaps[cap]]) {
                                        targetCaps[cap] = status;
                                    }
                                } else {
                                    targetCaps[cap] = status;
                                }
                            });
                        });
                });
            } else {
                angular.forEach(components[ctrl.target],
                    function (caps, status) {
                        angular.forEach(caps, function(cap) {
                            targetCaps[cap] = status;
                        });
                    });
            }
        }

        /**
         * This filter will check if a capability's status corresponds
         * to a status that is checked/selected in the UI. This filter
         * is meant to be used with the ng-repeat directive.
         * @param {Object} capability
         * @returns {Boolean} True if capability's status is selected
         */
        function filterStatus(capability) {
            var caps = ctrl.targetCapabilities;
            return ctrl.status.required &&
                caps[capability.id] === 'required' ||
                ctrl.status.advisory &&
                caps[capability.id] === 'advisory' ||
                ctrl.status.deprecated &&
                caps[capability.id] === 'deprecated' ||
                ctrl.status.removed &&
                caps[capability.id] === 'removed';
        }

        /**
         * This function will get the length of an Object/dict based on
         * the number of keys it has.
         * @param {Object} object
         * @returns {Number} length of object
         */
        function getObjectLength(object) {
            return Object.keys(object).length;
        }

        /**
         * This will open the modal that will show a list of all tests
         * belonging to capabilities with the selected status(es).
         */
        function openTestListModal() {
            $uibModal.open({
                templateUrl: '/components/guidelines/partials' +
                        '/testListModal.html',
                backdrop: true,
                windowClass: 'modal',
                animation: true,
                controller: 'TestListModalController as modal',
                size: 'lg',
                resolve: {
                    version: function () {
                        return ctrl.version.name.slice(0, -5);
                    },
                    version_file: function() {
                        return ctrl.version.file;
                    },
                    target: function () {
                        return ctrl.target;
                    },
                    status: function () {
                        return ctrl.status;
                    }
                }
            });
        }
        ctrl.getVersionList();
    }

    angular
        .module('refstackApp')
        .controller('TestListModalController', TestListModalController);

    TestListModalController.$inject = [
        '$uibModalInstance', '$http', 'version',
        'version_file', 'target', 'status',
        'refstackApiUrl'
    ];

    /**
     * Test List Modal Controller
     * This controller is for the modal that appears if a user wants to see the
     * test list corresponding to Interop WG capabilities with the selected
     * statuses.
     */
    function TestListModalController($uibModalInstance, $http, version,
        version_file, target, status, refstackApiUrl) {

        var ctrl = this;

        ctrl.version = version;
        ctrl.version_file = version_file;
        ctrl.target = target;
        ctrl.status = status;
        ctrl.close = close;
        ctrl.updateTestListString = updateTestListString;

        ctrl.aliases = true;
        ctrl.flagged = false;

        // Check if the API URL is absolute or relative.
        if (refstackApiUrl.indexOf('http') > -1) {
            ctrl.url = refstackApiUrl;
        } else {
            ctrl.url = location.protocol + '//' + location.host +
                refstackApiUrl;
        }

        /**
         * This function will close/dismiss the modal.
         */
        function close() {
            $uibModalInstance.dismiss('exit');
        }

        /**
         * This function will return a list of statuses based on which ones
         * are selected.
         */
        function getStatusList() {
            var statusList = [];
            angular.forEach(ctrl.status, function(value, key) {
                if (value) {
                    statusList.push(key);
                }
            });
            return statusList;
        }

        /**
         * This will get the list of tests from the API and update the
         * controller's test list string variable.
         */
        function updateTestListString() {
            var statuses = getStatusList();
            if (!statuses.length) {
                ctrl.error = 'No tests matching selected criteria.';
                return;
            }
            ctrl.testListUrl = [
                ctrl.url, '/guidelines/', ctrl.version_file, '/tests?',
                'target=', ctrl.target, '&',
                'type=', statuses.join(','), '&',
                'alias=', ctrl.aliases.toString(), '&',
                'flag=', ctrl.flagged.toString()
            ].join('');
            ctrl.testListRequest =
                $http.get(ctrl.testListUrl).
                    then(function successCallback(response) {
                        ctrl.error = null;
                        ctrl.testListString = response.data;
                        if (!ctrl.testListString) {
                            ctrl.testListCount = 0;
                        } else {
                            ctrl.testListCount =
                                ctrl.testListString.split('\n').length;
                        }
                    }, function errorCallback(response) {
                        ctrl.testListString = null;
                        ctrl.testListCount = null;
                        if (angular.isObject(response.data) &&
                            response.data.message) {
                            ctrl.error = 'Error retrieving test list: ' +
                                response.data.message;
                        } else {
                            ctrl.error = 'Unknown error retrieving test list.';
                        }
                    });
        }

        updateTestListString();
    }
})();
