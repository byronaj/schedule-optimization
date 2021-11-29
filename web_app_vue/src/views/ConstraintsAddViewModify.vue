<template>
    <div class="container is-fluid">
        <nav class="breadcrumb is-small" aria-label="breadcrumbs">
            <ul>
                <li><a href="/">Dashboard</a></li>
                <li class="is-active"><a href="#" aria-current="page">Scheduling Constraints</a></li>
            </ul>
        </nav>
    </div>

    <div class="container is-fluid">
        <div class="columns is-multiline">
            <div class="column is-10">
                <p class="title">Scheduling Constraints:</p>
            </div>

            <!--  Weekly staffing requirements  -->
            <div class="column is-3">
                <nav class="panel is-info">
                    <p class="panel-heading">
                        Shift Coverage Requirements
                    </p>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Mon:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.mon_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.mon_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.mon_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Tue:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.tue_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.tue_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.tue_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Wed:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.wed_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.wed_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.wed_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Thu:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.thu_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.thu_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.thu_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Fri:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.fri_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.fri_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.fri_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Sat:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.sat_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.sat_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.sat_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="columns">
                            <div class="column">
                                <div class="field is-horizontal">

                                    <div class="field-label is-normal">
                                        <label class="label" style="width: 40px">Sun:</label>
                                    </div>

                                    <div class="field-body">

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.sun_shift1"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">day shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.sun_shift2"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">second shift</p>
                                        </div>

                                        <div class="field">
                                            <p class="control">
                                                <input
                                                    class="input has-text-centered"
                                                    style="width: 70px"
                                                    type="text"
                                                    v-model="weekly_cover_instance.sun_shift3"
                                                />
                                            </p>
                                            <p class="help is-info has-text-centered">night shift</p>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <button class="button is-link is-outlined is-fullwidth" @click="getShiftCov">
                                <span><strong>undo changes</strong></span>
                            </button>
                        </div>
                    </div>
                    <div class="panel-block">
                        <div class="control">
                            <button class="button is-success is-outlined is-fullwidth" @click="submitShiftCov">
                                <span><strong>save changes</strong></span>
                            </button>
                        </div>
                    </div>

                </nav>
            </div>

            <!--  Penalized shift transitions  -->
            <div class="column is-6">
                <nav class="panel is-info">

                    <p class="panel-heading">
                        Penalized shift transitions
                    </p>

                    <div class="panel-block">
                        <p>
                            Undesirable transitions from shift to another.
                            For example, working a night shift that is directly followed by a day shift.
                            Setting importance to zero prevents the transition from occurring at all in the schedule.
                        </p>
                    </div>

                    <div class="panel-block" v-for="tc in transition_constraints" v-bind:key="tc.id">
                        <div class="field is-grouped">

                            <div class="field-label is-normal">
                                transition {{ tc.id }}
                            </div>

                            <div class="field-body">

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered"
                                            style="width: 100px"
                                            type="text"
                                            v-model="tc.previous_shift"
                                        />
                                    </p>
                                    <p class="label has-text-centered">from shift...</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered"
                                            style="width: 100px"
                                            type="text"
                                            v-model="tc.next_shift"
                                        />
                                    </p>
                                    <p class="label has-text-centered">...to shift</p>
                                </div>

                                <div class="field">

                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-background-warning-light"
                                            style="width: 100px"
                                            type="text"
                                            v-model="tc.penalty"
                                        />
                                    </p>
                                    <p class="label has-text-centered">importance</p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action -->
                                        <button class="button is-success is-outlined" @click="">
                                            <span>save changes</span>
                                        </button>
                                    </div>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--   TODO: implement button action     -->
                                        <button class="button is-danger is-outlined" @click="">
                                            <span>delete</span>
                                        </button>
                                    </div>
                                </div>

                            </div>

                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <!--   TODO: implement button action   -->
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span><strong>create new penalized transition</strong></span>
                            </button>
                        </div>
                    </div>

                </nav>
            </div>

<!--        Consecutive shift rules    -->
            <div class="column is-11">
                <nav class="panel is-info">
                    <p class="panel-heading">
                        Consecutive shift rules
                    </p>

                    <div class="panel-block">
                        <p>
                            Rules on the number of consecutive shifts of one type.
                            For example, at least one day off per week and at most two CONSECUTIVE days off.
                        </p>
                    </div>

                    <div class="panel-block" v-for="sequence in sequence_constraints" v-bind:key="sequence.id">
                        <div class="field is-grouped">

                            <div class="field-label">
                                rule {{ sequence.id }}
                            </div>

                            <div class="field-body">

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered"
                                            style="width: 70px"
                                            type="text"
                                            v-model="sequence.shift_id"
                                        />
                                    </p>
                                    <p class="label has-text-centered">shift</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-text-danger-dark has-background-danger-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sequence.hard_min"
                                        />
                                    </p>
                                    <p class="label has-text-centered">hard minimum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered  has-text-link-dark has-background-link-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sequence.soft_min"
                                        />
                                    </p>
                                    <p class="label has-text-centered">ideal minimum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-background-warning-light"
                                            style="width: 170px"
                                            type="text"
                                            v-model="sequence.min_penalty"
                                        />
                                    </p>
                                    <p class="label has-text-centered">importance of staying ABOVE the ideal min?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-background-warning-light"
                                            style="width: 170px"
                                            type="text"
                                            v-model="sequence.max_penalty"
                                        />
                                    </p>
                                    <p class="label has-text-centered">importance of staying BELOW the ideal max?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-text-link-dark has-background-link-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sequence.soft_max"
                                        />
                                    </p>
                                    <p class="label has-text-centered">ideal maximum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-text-danger-dark has-background-danger-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sequence.hard_max"
                                        />
                                    </p>
                                    <p class="label has-text-centered">hard maximum</p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action -->
                                        <button class="button is-success is-outlined" @click="">
                                            <span>save changes</span>
                                        </button>
                                    </div>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--   TODO: implement button action     -->
                                        <button class="button is-danger is-outlined" @click="">
                                            <span>delete</span>
                                        </button>
                                    </div>
                                </div>

                            </div>

                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <!--  TODO: implement button action   -->
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span><strong>create new consecutive shift rule</strong></span>
                            </button>
                        </div>
                    </div>

                </nav>
            </div>

<!--        Weekly sum constraints    -->
            <div class="column is-11">
                <nav class="panel is-info">
                    <p class="panel-heading">
                        Limits on the number of times a shift should be assigned each week:
                    </p>

                    <div class="panel-block">
                        <p>
                            Limits on the number of shifts of one type per week.
                            For example, at least one day off per week and at most three days off, but ideally two days off.
                        </p>
                    </div>

                    <div class="panel-block" v-for="sc in sum_constraints" v-bind:key="sc.id">
                        <div class="field is-grouped">

                            <div class="field-label">
                                limit {{ sc.id }}
                            </div>

                            <div class="field-body">

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered"
                                            style="width: 70px"
                                            type="text"
                                            v-model="sc.shift_id"
                                        />
                                    </p>
                                    <p class="label has-text-centered">shift</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-text-danger-dark has-background-danger-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sc.hard_min"
                                        />
                                    </p>
                                    <p class="label has-text-centered">hard minimum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered  has-text-link-dark has-background-link-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sc.soft_min"
                                        />
                                    </p>
                                    <p class="label has-text-centered">ideal minimum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-background-warning-light"
                                            style="width: 170px"
                                            type="text"
                                            v-model="sc.min_penalty"
                                        />
                                    </p>
                                    <p class="label has-text-centered">importance of staying ABOVE the ideal min?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-background-warning-light"
                                            style="width: 170px"
                                            type="text"
                                            v-model="sc.max_penalty"
                                        />
                                    </p>
                                    <p class="label has-text-centered">importance of staying BELOW the ideal max?</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-text-link-dark has-background-link-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sc.soft_max"
                                        />
                                    </p>
                                    <p class="label has-text-centered">ideal maximum</p>
                                </div>

                                <div class="field">
                                    <p class="control">
                                        <input
                                            class="input has-text-centered has-text-danger-dark has-background-danger-light"
                                            style="width: 130px"
                                            type="text"
                                            v-model="sc.hard_max"
                                        />
                                    </p>
                                    <p class="label has-text-centered">hard maximum</p>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--  TODO: implement button action -->
                                        <button class="button is-success is-outlined" @click="">
                                            <span>save changes</span>
                                        </button>
                                    </div>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <!--   TODO: implement button action     -->
                                        <button class="button is-danger is-outlined" @click="">
                                            <span>delete</span>
                                        </button>
                                    </div>
                                </div>

                            </div>

                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="control">
                            <!--  TODO: implement button action   -->
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span><strong>create new limit</strong></span>
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
import { toast } from "bulma-toast";

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
                    this.weekly_cover_instance = response.data
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
                })
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
                })
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
                })
        }
    }
};
</script>

<style scoped>

</style>
