<template>
    <div class="container is-fluid">
        <div class="columns is-multiline">

            <!--  COLUMN: Title  -->
            <div class="column is-10 is-offset-1">
                <p class="title is-2 pt-2">Scheduling Constraints</p>
            </div>

            <!--  COLUMN: Penalized Shift Transitions  -->
            <div class="column is-9 is-offset-1">
                <article class="panel">
                    <p class="panel-heading">Penalized Shift Transitions</p>

                    <div class="panel-block">
                        <p>Undesirable transitions from shift to another. For example, working a night shift that is directly followed by a day shift. Setting importance to zero prevents the transition from occurring at all in the schedule.</p>
                    </div>

<!--                    <div class="panel-block" v-for="tc in penalized_transitions.transition_constraints" v-bind:key="tc.id">-->
                    <div class="panel-block" v-for="tc in transition_constraints" v-bind:key="tc.id">
                        <div class="field is-grouped">

                            <div class="field-label">Transition #{{ tc.id }}</div>

                            <div class="field-body">
                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered" type="text" v-model="tc.previous_shift" /> &lt;!&ndash; style="width: 100px" &ndash;&gt;-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="previous_shift" v-model="tc.previous_shift">
                                            <option value="0">Off</option>
                                            <option value="1">First</option>
                                            <option value="2">Second</option>
                                            <option value="3">Third</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">From Shift...</label>
                                </div>

                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered" type="text" v-model="tc.next_shift" /> &lt;!&ndash; style="width: 100px" &ndash;&gt;-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="next_shift" v-model="tc.next_shift">
                                            <option value="0">Off</option>
                                            <option value="1">First</option>
                                            <option value="2">Second</option>
                                            <option value="3">Third</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">...To Shift</label>
                                </div>

                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered has-background-warning-light" type="text" v-model="tc.penalty" /> &lt;!&ndash; style="width: 100px" &ndash;&gt;-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="penalty" v-model="tc.penalty">
<!--                                            <option>{{ tc.penalty }}</option> &lt;!&ndash; delete this line to stop showing current numerical value &ndash;&gt;-->
<!--                                            <option value="3">Low</option>-->
                                            <option value="4">Low</option>
                                            <option value="6">Medium</option>
                                            <option value="20">High</option>
                                            <option value="0">Mandatory</option>
                                        </select>
                                    </div>

                                    <label class="label has-text-centered">Importance</label>
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
<!--                                <div class="field">-->
<!--                                    <p class="control">-->
<!--                                        <button class="button is-success" @click="submitTransition"> &lt;!&ndash; @click="" &ndash;&gt;-->
<!--                                            <span class="icon"><i class="fas fa-check"></i></span>-->
<!--                                            <span><strong>Save Changes</strong></span>-->
<!--                                        </button>-->
<!--                                    </p>-->
<!--                                </div>-->

                            </div>

                        </div>

                    </div>

                    <div class="panel-block">

<!--                        <div class="field is-grouped">-->
<!--                            <p class="control">-->
<!--                                <button class="button is-primary is-light"> &lt;!&ndash; @click="" &ndash;&gt;-->
<!--                                    <span class="icon"><i class="fas fa-plus"></i></span>-->
<!--                                    <span><strong>Create New Penalized Transition</strong></span>-->
<!--                                </button>-->
<!--                            </p>-->
<!--                            <p class="control">-->
<!--                                <button class="button is-link"> &lt;!&ndash; @click="" &ndash;&gt;-->
<!--                                    <span class="icon"><i class="fas fa-undo"></i></span>-->
<!--                                    <span><strong>Undo Changes</strong></span>-->
<!--                                </button>-->
<!--                            </p>-->
<!--                        </div>-->

                        <div class="control buttons">
                            <!--  TODO: implement button action  -->
                            <button class="button is-primary is-light is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-plus"></i></span>
                                <span><strong>Create New Penalized Transition</strong></span>
                            </button>
                            <button class="button is-link is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-undo"></i></span>
                                <span><strong>Undo Changes</strong></span>
                            </button>
                            <button class="button is-success is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-check"></i></span>
                                <span><strong>Save Changes</strong></span>
                            </button>
                        </div>
                    </div>
                </article>
            </div>

            <!--  COLUMN: Consecutive Shift Rules  -->
            <div class="column is-9 is-offset-1">
                <article class="panel">
                    <p class="panel-heading">Consecutive Shift Rules</p>

                    <div class="panel-block">
                        <p>Rules on the number of consecutive shifts of one type. For example, at least one day off per week and at most two CONSECUTIVE days off.</p>
                    </div>

                    <div class="panel-block" v-for="sequence in sequence_constraints" v-bind:key="sequence.id">
                        <div class="field is-grouped">
                            <div class="field-label">Rule #{{ sequence.id }}</div>

                            <div class="field-body">
                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered" style="width: 70px" type="text" v-model="sequence.shift_id" />-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="shift_id" v-model="sequence.shift_id">
                                            <option value="0">Off</option>
                                            <option value="1">First</option>
                                            <option value="2">Second</option>
                                            <option value="3">Third</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">Shift</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 80px" type="text" v-model="sequence.hard_min" />
                                    </p>
                                    <label class="label has-text-centered">At Least</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sequence.soft_min" />
                                    </p>
                                    <label class="label has-text-centered">Ideal Minimum</label>
                                </div>

                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered has-background-warning-light" style="width: 220px" type="text" v-model="sequence.min_penalty" />-->
<!--                                    </p>-->

                                    <!-- this works; no time to finish it now though -->
                                    <div class="select has-background-warning-light">
                                        <select name="min_penalty" v-model="sequence.min_penalty">
<!--                                            <option>{{ sequence.min_penalty }}</option>-->
                                            <option value="3">Low</option>
                                            <option value="6">Medium</option>
                                            <option value="20">High</option>
                                            <option value="0">Mandatory</option>
                                        </select>
                                    </div>

                                    <label class="label has-text-centered">Importance of keeping ABOVE Ideal Min?</label>
                                </div>

                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered has-background-warning-light" style="width: 220px" type="text" v-model="sequence.max_penalty" />-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="max_penalty" v-model="sequence.max_penalty">
<!--                                            <option>{{ sequence.max_penalty }}</option> &lt;!&ndash; delete this line to stop showing current numerical value &ndash;&gt;-->
                                            <option value="3">Low</option>
                                            <option value="5">Medium</option>
<!--                                            <option value="6">Medium</option>-->
                                            <option value="20">High</option>
                                            <option value="0">Mandatory</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">Importance of keeping BELOW Ideal Max?</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sequence.soft_max" />
                                    </p>
                                    <label class="label has-text-centered">Ideal Maximum</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 80px" type="text" v-model="sequence.hard_max" />
                                    </p>
                                    <label class="label has-text-centered">At Most</label>
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
                        <div class="control buttons">
                            <!--  TODO: implement button action  -->
                            <button class="button is-primary is-light is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-plus"></i></span>
                                <span><strong>Create New Consecutive Shift Rule</strong></span>
                            </button>
                            <button class="button is-link is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-undo"></i></span>
                                <span><strong>Undo Changes</strong></span>
                            </button>
                            <button class="button is-success is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-check"></i></span>
                                <span><strong>Save Changes</strong></span>
                            </button>
                        </div>
                    </div>
                </article>
            </div>

            <!--  COLUMN: Weekly Sum Constraints  -->
            <div class="column is-9 is-offset-1">
                <article class="panel">
                    <p class="panel-heading">Limits On Number Of Times A Shift Should Be Assigned Each Week</p>

                    <div class="panel-block">
                        <p>Limits on the number of shifts of one type per week. For example, at least one day off per week and at most three days off, but ideally two days off.</p>
                    </div>

                    <div class="panel-block" v-for="sc in sum_constraints" v-bind:key="sc.id">
                        <div class="field is-grouped">
                            <div class="field-label">Limit #{{ sc.id }}</div>

                            <div class="field-body">
                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered" style="width: 70px" type="text" v-model="sc.shift_id" />-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="shift_id" v-model="sc.shift_id">
                                            <option value="0">Off</option>
                                            <option value="1">First</option>
                                            <option value="2">Second</option>
                                            <option value="3">Third</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">Shift</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 80px" type="text" v-model="sc.hard_min" />
                                    </p>
                                    <label class="label has-text-centered">At Least</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sc.soft_min" />
                                    </p>
                                    <label class="label has-text-centered">Ideal Minimum</label>
                                </div>

                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered has-background-warning-light" style="width: 220px" type="text" v-model="sc.min_penalty" />-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="min_penalty" v-model="sc.min_penalty">
<!--                                            <option>{{ sc.min_penalty }}</option> &lt;!&ndash; delete this line to stop showing current numerical value &ndash;&gt;-->
                                            <option value="3">Low</option>
<!--                                            <option value="6">Medium</option>-->
                                            <option value="7">Medium</option>
                                            <option value="20">High</option>
                                            <option value="0">Mandatory</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">Importance of keeping ABOVE Ideal Min?</label>
                                </div>

                                <div class="field">
<!--                                    <p class="control">-->
<!--                                        <input class="input has-text-centered has-background-warning-light" style="width: 220px" type="text" v-model="sc.max_penalty" />-->
<!--                                    </p>-->
                                    <div class="select has-background-warning-light">
                                        <select name="max_penalty" v-model="sc.max_penalty">
<!--                                            <option>{{ sc.max_penalty }}</option> &lt;!&ndash; delete this line to stop showing current numerical value &ndash;&gt;-->
<!--                                            <option value="3">Low</option>-->
                                            <option value="4">Low</option>
                                            <option value="6">Medium</option>
                                            <option value="20">High</option>
                                            <option value="0">Mandatory</option>
                                        </select>
                                    </div>
                                    <label class="label has-text-centered">Importance of keeping BELOW Ideal Max?</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sc.soft_max" />
                                    </p>
                                    <label class="label has-text-centered">Ideal Maximum</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 80px" type="text" v-model="sc.hard_max" />
                                    </p>
                                    <label class="label has-text-centered">At Most</label>
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
                        <div class="control buttons">
                            <!--  TODO: implement button action  -->
                            <button class="button is-primary is-light is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-plus"></i></span>
                                <span><strong>Create New Weekly Sum Constraint</strong></span>
                            </button>
                            <button class="button is-info is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-undo"></i></span>
                                <span><strong>Undo Changes</strong></span>
                            </button>
                            <button class="button is-success is-fullwidth"> <!-- @click="" -->
                                <span class="icon"><i class="fas fa-check"></i></span>
                                <span><strong>Save Changes</strong></span>
                            </button>
                        </div>
                    </div>
                </article>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import VueNextSelect from 'vue-next-select'


export default {
    name: 'ConstraintsAddViewModify',
    data() {
        return {
            // penalized_transitions: {
            //     transition_constraints: [],
            // },
            // continuous_sequence: {
            //     sequence_constraints: [],
            // },
            // weekly_sum: {
            //     sum_constraints: [],
            // },
            transition_constraints: [],
            sequence_constraints: [],
            sum_constraints: [],
            weekly_cover_instance: {},
        };
    },
    components: {
        'vue-select': VueNextSelect,
    },
    mounted() {
        this.getShiftCov();
        this.getSequences();
        this.getWeeklySums();
        this.getTransitions();
    },
    methods: {
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
        getTransitions() {
            axios
                .get(`/api/v1/transitions`)
                .then((response) => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.transition_constraints.push(response.data[i]);
                        // this.penalized_transitions.transition_constraints.push(response.data[i]);
                    }
                })
                .catch((error) => {
                    console.log(JSON.stringify(error));
                });
        },
        // submitTransition() {
        //     const tcID = this.penalized_transitions.transition_constraints.tc.id
        //     axios
        //         .patch(`/api/v1/transitions/${tcID}/`, this.penalized_transitions.transition_constraints)
        //         .then((response) => {
        //             toast({
        //                 message: 'Changes saved',
        //                 type: 'is-success',
        //                 dismissible: true,
        //                 pauseOnHover: true,
        //                 duration: 2000,
        //                 position: 'bottom-right',
        //             });
        //         })
        //         .catch((error) => {
        //             console.log(JSON.stringify(error));
        //         });
        // },
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
        // updateSequence() {
        //     const id = this.sequence_constraints.id;
        //     axios
        //         .patch(`/api/v1/sequences/${sequence.id}/`,
        //             {
        //                 shift_id: 'shift_id',
        //                 hard_min: 'hard_min',
        //                 soft_min: 'soft_min',
        //                 min_penalty: 'min_penalty',
        //                 soft_max: 'soft_max',
        //                 hard_max: 'hard_max',
        //                 max_penalty: 'max_penalty',
        //             })
        //         .then((response) => {
        //             toast({
        //                 message: 'Changes saved',
        //                 type: 'is-success',
        //                 dismissible: true,
        //                 pauseOnHover: true,
        //                 duration: 2000,
        //                 position: 'bottom-right',
        //             });
        //         })
        //         .catch((error) => {
        //             console.log(JSON.stringify(error));
        //         });
        // },
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
        // deletePenalizedShiftTransition() {
        // 	const NAME = this.NAME;
        // },
        // deleteConsecutiveShiftRule() {
        // 	const NAME = this.NAME;
        // },
        // deleteWeeklySumConstraint() {
        // 	const NAME = this.NAME;
        // },
    },
};
</script>

<style scoped></style>
