<template>

    <div class="container is-fluid">
        <div class="columns is-multiline">
            <div class="column is-centered is-full">
                <p class="title has-text-centered is-1">Scheduling Constraints</p>
            </div>

            <!--  Penalized Shift Transitions  -->
            <div class="column is-10 is-offset-1">
                <nav class="panel is-info">
                    <p class="panel-heading">Penalized Shift Transitions</p>

                    <div class="panel-block">
                        <p>
                            Undesirable transitions from shift to another. For example, working a night shift that is directly followed by a day shift. Setting importance to zero prevents the
                            transition from occurring at all in the schedule.
                        </p>
                    </div>

                    <div class="panel-block" v-for="tc in transition_constraints" v-bind:key="tc.id">
                        <div class="field is-grouped">
                            <div class="field-label is-normal">Transition #{{ tc.id }}</div>

                            <div class="field-body">
                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" style="width: 100px" type="text" v-model="tc.previous_shift" />
                                    </p>
                                    <p class="label has-text-centered">From Shift...</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" style="width: 100px" type="text" v-model="tc.next_shift" />
                                    </p>
                                    <p class="label has-text-centered">...To Shift</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 100px" type="text" v-model="tc.penalty" />
                                    </p>
                                    <p class="label has-text-centered">Importance</p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action  -->
                                        <button class="button is-success is-outlined"> <!-- @click="" -->
                                            <span class="icon"><i class="fas fa-check"></i></span>
                                            <span>Save Changes</span>
                                        </button>
                                    </div>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action  -->
                                        <button class="button is-danger is-outlined"> <!-- @click="" -->
                                            <span>Delete</span>
                                            <span class="icon"><i class="fas fa-times"></i></span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <!--  TODO: implement button action  -->
                            <button class="button is-success is-outlined is-fullwidth"> <!-- @click="" -->
                                <span><strong>Create New Penalized Transition</strong></span>
                            </button>
                        </div>
                    </div>
					<div class="panel-block">
                        <div class="control">
                            <button class="button is-link is-outlined is-fullwidth" @click="">
                                <span><strong>Undo Changes</strong></span>
                            </button>
                        </div>
                    </div>
                    <div class="panel-block">
                        <div class="control">
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span class="icon"><i class="fas fa-check"></i></span>
                                <span><strong>Save Changes</strong></span>
                            </button>
                        </div>
                    </div>
                </nav>
            </div>

            <!--  Consecutive Shift Rules  -->
            <div class="column is-10 is-offset-1">
                <nav class="panel is-info">
                    <p class="panel-heading">Consecutive Shift Rules</p>

                    <div class="panel-block">
                        <p>Rules on the number of consecutive shifts of one type. For example, at least one day off per week and at most two CONSECUTIVE days off.</p>
                    </div>

                    <div class="panel-block" v-for="sequence in sequence_constraints" v-bind:key="sequence.id">
                        <div class="field is-grouped">
                            <div class="field-label">Rule #{{ sequence.id }}</div>

                            <div class="field-body">
                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" style="width: 70px" type="text" v-model="sequence.shift_id" />
                                    </p>
                                    <p class="label has-text-centered">Shift</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sequence.hard_min" />
                                    </p>
                                    <p class="label has-text-centered">At Least</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sequence.soft_min" />
                                    </p>
                                    <p class="label has-text-centered">Ideal Minimum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sequence.min_penalty" />
                                    </p>

                                    <!-- <div class="control dropdown"> -->

                                        <!-- <div class="dropdown-trigger">
                                            <button class="button has-background-warning-light" @click="importanceDDClick">
                                                <span>Importance</span>
                                                <span class="icon is-small"><i class="fas fa-angle-down"></i></span>
                                            </button>
                                        </div> -->

                                        <!-- <div class="dropdown-menu has-background-warning-light" role="menu" v-if="importanceDD"> -->
										<select class="has-background-warning-light">
                                            <div class="dropdown-content has-background-warning-light">
                                                <option class="dropdown-item" value="3">Low</option>
                                                <option class="dropdown-item" value="6">Medium</option>
                                                <option class="dropdown-item" value="20">High</option>
                                                <option class="dropdown-item" value="0">Mandatory</option>
                                            </div>
										</select>
                                        <!-- </div> -->

                                    <!-- </div> -->

                                    <p class="label has-text-centered">Importance of keeping ABOVE Ideal Min?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sequence.max_penalty" />
                                    </p>
                                    <p class="label has-text-centered">Importance of keeping BELOW Ideal Max?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sequence.soft_max" />
                                    </p>
                                    <p class="label has-text-centered">Ideal Maximum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sequence.hard_max" />
                                    </p>
                                    <p class="label has-text-centered">At Most</p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action  -->
                                        <button class="button is-danger is-outlined"> <!-- @click="" -->
                                            <span>Delete</span>
                                            <span class="icon"><i class="fas fa-times"></i></span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <!--  TODO: implement button action  -->
                            <button class="button is-success is-outlined is-fullwidth"> <!-- @click="" -->
                                <span><strong>Create New Consecutive Shift Rule</strong></span>
                            </button>
                        </div>
                    </div>
					<div class="panel-block">
                        <div class="control">
                            <button class="button is-link is-outlined is-fullwidth" @click="">
                                <span><strong>Undo Changes</strong></span>
                            </button>
                        </div>
                    </div>
                    <div class="panel-block">
                        <div class="control">
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span class="icon"><i class="fas fa-check"></i></span>
                                <span><strong>Save Changes</strong></span>
                            </button>
                        </div>
                    </div>
                </nav>
            </div>

            <!-- Weekly Sum Constraints/Limits -->
            <div class="column is-10 is-offset-1">
                <nav class="panel is-info">
                    <p class="panel-heading">Weekly Sum Limits</p>

                    <div class="panel-block">
                        <p>Limits on the number of shifts of one type per week. For example, at least one day off per week and at most three days off, but ideally two days off.</p>
                    </div>

                    <div class="panel-block" v-for="sc in sum_constraints" v-bind:key="sc.id">
                        <div class="field is-grouped">
                            <div class="field-label">Limit #{{ sc.id }}</div>

                            <div class="field-body">
                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" style="width: 70px" type="text" v-model="sc.shift_id" />
                                    </p>
                                    <p class="label has-text-centered">Shift</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sc.hard_min" />
                                    </p>
                                    <p class="label has-text-centered">At Least</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sc.soft_min" />
                                    </p>
                                    <p class="label has-text-centered">Ideal Minimum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sc.min_penalty" />
                                    </p>
                                    <p class="label has-text-centered">Importance of keeping ABOVE Ideal Min?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sc.max_penalty" />
                                    </p>
                                    <p class="label has-text-centered">Importance of keeping BELOW Ideal Max?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sc.soft_max" />
                                    </p>
                                    <p class="label has-text-centered">Ideal Maximum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sc.hard_max" />
                                    </p>
                                    <p class="label has-text-centered">At Most</p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action  -->
                                        <button class="button is-danger is-outlined"> <!-- @click="" -->
                                            <span>Delete</span>
                                            <span class="icon"><i class="fas fa-times"></i></span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <!--  TODO: implement button action  -->
                            <button class="button is-success is-outlined is-fullwidth"> <!-- @click="" -->
                                <span><strong>Create New Weekly Sum Limit</strong></span>
                            </button>
                        </div>
                    </div>
					<div class="panel-block">
                        <div class="control">
                            <button class="button is-link is-outlined is-fullwidth" @click="">
                                <span><strong>Undo Changes</strong></span>
                            </button>
                        </div>
                    </div>
                    <div class="panel-block">
                        <div class="control">
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span class="icon"><i class="fas fa-check"></i></span>
                                <span><strong>Save Changes</strong></span>
                            </button>
                        </div>
                    </div>
                </nav>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { toast } from 'bulma-toast';

    export default {
        name: 'ConstraintsAddViewModify',
        data() {
            return {
                weekly_cover_instance: {},
                sequence_constraints: [],
                sum_constraints: [],
                transition_constraints: [],
            };
        },
        mounted() {
            this.getShiftCov();
            this.getSequences();
            this.getWeeklySums();
            this.getTransitions();
        },
        methods: {
            importanceDDClick() {
                this.importanceDD = !this.importanceDD
            },
            getShiftCov() {
                axios
                    .get(`/api/v1/coverages/1/`)
                    .then((response) => {
                        this.weekly_cover_instance = response.data;
                    })
                    .catch((error) => {
                        console.log(JSON.stringify(error));
                    });
            },
            submitShiftCov() {
                axios
                    .patch(`/api/v1/coverages/1/`, this.weekly_cover_instance)
                    .then((response) => {
                        toast({
                            message: 'Changes saved',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        });
                        this.$router.push('/constraints-avm');
                    })
                    .catch((error) => {
                        console.log(JSON.stringify(error));
                    });
            },
            getSequences() {
                axios
                    .get(`/api/v1/sequences`)
                    .then((response) => {
                        for (let i = 0; i < response.data.length; i++) {
                            this.sequence_constraints.push(response.data[i]);
                        }
                    })
                    .catch((error) => {
                        console.log(JSON.stringify(error));
                    });
            },
            getWeeklySums() {
                axios
                    .get(`/api/v1/weeklysums`)
                    .then((response) => {
                        for (let i = 0; i < response.data.length; i++) {
                            this.sum_constraints.push(response.data[i]);
                        }
                    })
                    .catch((error) => {
                        console.log(JSON.stringify(error));
                    });
            },
            getTransitions() {
                axios
                    .get(`/api/v1/transitions`)
                    .then((response) => {
                        for (let i = 0; i < response.data.length; i++) {
                            this.transition_constraints.push(response.data[i]);
                        }
                    })
                    .catch((error) => {
                        console.log(JSON.stringify(error));
                    });
            },
        },
    };
</script>

<style scoped></style>
