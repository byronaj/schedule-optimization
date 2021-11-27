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
                        <div class="columns is-vcentered">
                            <div class="column">
                                <div class="field is-horizontal">
                                    <div class="field-label is-normal">
                                        <label class="label">Mon:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.mon_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.mon_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.mon_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
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
                                        <label class="label">Tue:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.tue_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.tue_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.tue_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
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
                                        <label class="label">Wed:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.wed_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.wed_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.wed_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
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
                                        <label class="label">Thu:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.thu_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.thu_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.thu_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
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
                                        <label class="label">Fri:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.fri_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.fri_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.fri_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
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
                                        <label class="label">Sat:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.sat_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.sat_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.sat_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
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
                                        <label class="label">Sun:</label>
                                    </div>
                                    <div class="field-body">
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.sun_shift1" />
                                            </p>
                                            <p class="help is-info">day shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.sun_shift2" />
                                            </p>
                                            <p class="help is-info">second shift</p>
                                        </div>
                                        <div class="field">
                                            <p class="control">
                                                <input class="input is-small has-text-centered" type="text" v-model="weekly_cover_instance.sun_shift3" />
                                            </p>
                                            <p class="help is-info">night shift</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="panel-block">
                        <div class="field is-grouped">
                            <div class="control">
                                <button class="button is-link is-outlined" @click="getShiftCov">
                                    <span>reset form</span>
                                </button>
                            </div>
                            <div class="control">
                                <button class="button is-success is-outlined" @click="submitShiftCov">
                                    <span>save changes</span>
                                </button>
                            </div>
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
                        </p>
                    </div>

                    <div class="panel-block" v-for="tc in transition_constraints" v-bind:key="tc.id">
                        <div class="field is-grouped">
                            <div class="field-label">
                                transition {{ tc.id }}
                            </div>
                            <div class="field-body">
                                <div class="field">
                                    <p class="control">
                                        <input class="input has-text-centered" type="text" v-model="tc.previous_shift" />
                                    </p>
                                    <p class="label">from shift...</p>
                                </div>
                                <div class="field">

                                    <p class="control">
                                        <input class="input has-text-centered" type="text" v-model="tc.next_shift" />
                                    </p>
                                    <p class="label">...to shift</p>
                                </div>
                                <div class="field">

                                    <p class="control">
                                        <input class="input has-text-centered has-background-warning-light" type="text" v-model="tc.penalty" />
                                    </p>
                                    <p class="label">importance</p>
                                </div>
                                <div class="field">
                                    <div class="control">
<!--                                    TODO: implement button action -->
                                        <button class="button is-success is-outlined" @click="">
                                            <span>save changes</span>
                                        </button>
                                    </div>
                                </div>
                                <div class="field">
                                    <div class="control">
<!--                                    TODO: implement button action     -->
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
<!--                        TODO: implement button action   -->
                            <button class="button is-success is-outlined is-fullwidth" @click="">
                                <span>create new penalized transition</span>
                            </button>
                        </div>
                    </div>
                </nav>
            </div>

<!--        Consecutive shift rules    -->
            <div class="column is-two-fifths">
                <div class="card">
                    <header class="card-header has-background-info-dark">
                        <p class="card-header-title has-text-info-light">Consecutive shift rules:</p>
                    </header>
                    <div class="card-content">
                        <div class="content">
                            <div class="box">
                                description goes here
                            </div>
                            <table class="table is-bordered is-hoverable" v-for="sequence in sequence_constraints" v-bind:key="sequence.id">
                                <thead>
                                <tr>
                                    <th class="is-size-6 has-text-centered has-text-light has-background-dark">
                                        Rule {{ sequence.id }}
                                    </th>
                                </tr>
                                </thead>
                                <tbody >
                                <tr>
                                    <th class="is-size-6 has-text-right">Shift</th>
                                    <td class="has-text-centered">{{ sequence.shift_id }}</td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-danger-dark has-background-danger-light">Hard Minimum</th>
                                    <td class="has-text-centered has-text-danger-dark has-background-danger-light">
                                        {{ sequence.hard_min  }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-link-dark has-background-link-light">Ideal Minimum</th>
                                    <td class="has-text-centered has-text-link-dark has-background-link-light">
                                        {{ sequence.soft_min  }}
                                    </td>
                                </tr>
                                <tr>
                                    <th  class="is-size-6 has-text-right has-background-warning-light">Importance of staying ABOVE the ideal min?</th>
                                    <td class="has-text-centered has-background-warning-light">
                                        {{ sequence.min_penalty }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-background-warning-light">Importance of staying BELOW the ideal max?</th>
                                    <td class="has-text-centered has-background-warning-light">
                                        {{ sequence.max_penalty }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-link-dark has-background-link-light">Ideal Maximum</th>
                                    <td class="has-text-centered has-text-link-dark has-background-link-light">
                                        {{ sequence.soft_max }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-danger-dark has-background-danger-light">Hard Maximum</th>
                                    <td class="has-text-centered has-text-danger-dark has-background-danger-light">
                                        {{ sequence.hard_max }}
                                    </td>
                                </tr>
                                </tbody>
                                <tfoot>

                                </tfoot>
                            </table>
                        </div>
                    </div>
                    <footer class="card-footer has-background-success-dark">
                        <router-link to="/coverage-req" class="card-footer-item has-text-success-light">
                            click to add another
                        </router-link>
                    </footer>
                </div>
            </div>

            <div class="column is-two-fifths">
                <div class="card">
                    <header class="card-header has-background-info-dark">
                        <p class="card-header-title has-text-info-light">
                            Limits on the number of times a shift should be assigned each week:</p>
                    </header>
                    <div class="card-content">
                        <div class="content">
                            <div class="box">
                                description goes here
                            </div>
                            <table class="table is-bordered is-hoverable" v-for="sc in sum_constraints" v-bind:key="sc.id">
                                <thead>
                                <tr>
                                    <th class="is-size-6 has-text-centered has-text-light has-background-dark">
                                        Limit {{ sc.id }}
                                    </th>
                                </tr>
                                </thead>
                                <tbody >
                                <tr>
                                    <th class="is-size-6 has-text-right">Shift</th>
                                    <td class="has-text-centered">{{ sc.shift_id }}</td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-danger-dark has-background-danger-light">Hard Minimum</th>
                                    <td class="has-text-centered has-text-danger-dark has-background-danger-light">
                                        {{ sc.hard_min  }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-link-dark has-background-link-light">Ideal Minimum</th>
                                    <td class="has-text-centered has-text-link-dark has-background-link-light">
                                        {{ sc.soft_min  }}
                                    </td>
                                </tr>
                                <tr>
                                    <th  class="is-size-6 has-text-right has-background-warning-light">Importance of staying ABOVE the ideal min?</th>
                                    <td class="has-text-centered has-background-warning-light">
                                        {{ sc.min_penalty }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-background-warning-light">Importance of staying BELOW the ideal max?</th>
                                    <td class="has-text-centered has-background-warning-light">
                                        {{ sc.max_penalty }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-link-dark has-background-link-light">Ideal Maximum</th>
                                    <td class="has-text-centered has-text-link-dark has-background-link-light">
                                        {{ sc.soft_max }}
                                    </td>
                                </tr>
                                <tr>
                                    <th class="is-size-6 has-text-right has-text-danger-dark has-background-danger-light">Hard Maximum</th>
                                    <td class="has-text-centered has-text-danger-dark has-background-danger-light">
                                        {{ sc.hard_max }}
                                    </td>
                                </tr>
                                </tbody>
                                <tfoot>

                                </tfoot>
                            </table>
                        </div>
                    </div>
                    <footer class="card-footer has-background-success-dark">
                        <router-link to="/coverage-req" class="card-footer-item has-text-success-light">
                            click to add another
                        </router-link>
                    </footer>
                </div>
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
