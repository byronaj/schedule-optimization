<template>
    <div class="container is-fluid">
        <div class="columns is-multiline">

            <!--  COLUMN: Title  -->
            <div class="column is-10 is-offset-1">
                <p class="title has-text-centered is-1 pt-2">Scheduling Constraints</p>
            </div>

            <!--  COLUMN: Penalized Shift Transitions  -->
            <div class="column is-10 is-offset-1">
                <article class="panel">
                    <p class="panel-heading">Penalized Shift Transitions</p>

                    <div class="panel-block">
                        <p>Undesirable transitions from shift to another. For example, working a night shift that is directly followed by a day shift. Setting importance to zero prevents the transition from occurring at all in the schedule.</p>
                    </div>

                    <div class="panel-block" v-for="tc in transition_constraints" v-bind:key="tc.id"> <!-- class=" field" -->
                        <div class="field is-grouped">

                            <div class="field-label">Transition #{{ tc.id }}</div> <!-- class=" is-normal" -->

                            <div class="field-body">
                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" type="text" v-model="tc.previous_shift" /> <!-- style="width: 100px" -->
                                    </p>
                                    <label class="label has-text-centered">From Shift...</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" type="text" v-model="tc.next_shift" /> <!-- style="width: 100px" -->
                                    </p>
                                    <label class="label has-text-centered">...To Shift</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" type="text" v-model="tc.penalty" /> <!-- style="width: 100px" -->
                                    </p>
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


                            </div>

                        </div>

                    </div>

                    <div class="panel-block">
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
            <div class="column is-10 is-offset-1">
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
                                    <p class="control">
                                        <input class="input has-text-centered" style="width: 70px" type="text" v-model="sequence.shift_id" />
                                    </p>
                                    <label class="label has-text-centered">Shift</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sequence.hard_min" />
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
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sequence.min_penalty" />
                                    </p>

                                    <!-- <div class="control">
                                        <div class="select is-normal has-background-warning-light">
                                            <select class="has-text-centered has-background-warning-light">
                                                    <option class="has-text-info" value="3">Low (3)</option>
                                                    <option class="has-text-info" value="6">Medium (6)</option>
                                                    <option class="has-text-info" value="20">High (20)</option>
                                                    <option class="has-text-danger" value="0">Mandatory (0)</option>
                                            </select>
                                        </div>
                                    </div> -->

                                    <label class="label has-text-centered">Importance of keeping ABOVE Ideal Min?</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sequence.max_penalty" />
                                    </p>
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
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sequence.hard_max" />
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
            <div class="column is-10 is-offset-1">
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
                                    <p class="control">
                                        <input class="input has-text-centered" style="width: 70px" type="text" v-model="sc.shift_id" /> <!-- style="width: 70px" -->
                                    </p>
                                    <label class="label has-text-centered">Shift</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sc.hard_min" /> <!-- style="width: 130px" -->
                                    </p>
                                    <label class="label has-text-centered">At Least</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sc.soft_min" /> <!-- style="width: 130px" -->
                                    </p>
                                    <label class="label has-text-centered">Ideal Minimum</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sc.min_penalty" /> <!-- style="width: 170px" -->
                                    </p>
                                    <label class="label has-text-centered">Importance of keeping ABOVE Ideal Min?</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" style="width: 170px" type="text" v-model="sc.max_penalty" /> <!-- style="width: 170px" -->
                                    </p>
                                    <label class="label has-text-centered">Importance of keeping BELOW Ideal Max?</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-link-dark has-background-link-light" style="width: 130px" type="text" v-model="sc.soft_max" /> <!-- style="width: 130px" -->
                                    </p>
                                    <label class="label has-text-centered">Ideal Maximum</label>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered has-text-danger-dark has-background-danger-light" style="width: 130px" type="text" v-model="sc.hard_max" /> <!-- style="width: 130px" -->
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
                        }
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
