<template>
    <Modal @close="toggleShowModal">
        <header class="modal-card-head">
            <p class="modal-card-title">Shift Coverage Requirements</p>
            <button class="delete" aria-label="close" @click="toggleShowModal"></button>
        </header>

        <section class="modal-card-body" style="color: black">
            <nav class="panel">
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

            </nav>
        </section>

        <footer class="modal-card-foot">
            <button class="button is-success" @click="submitShiftCov">save</button>
            <button class="button is-warning" @click="getShiftCov">clear changes</button>
            <button class="button is-danger" aria-label="close" @click="toggleShowModal">cancel</button>
        </footer>

    </Modal>
</template>

<script>
import axios from 'axios';

import Modal from '@/components/Modal.vue';
import { toast } from "bulma-toast";

export default {
    components: { Modal },
    name: "ShiftCoverage",
    data() {
        return {
            weekly_cover_instance: {},
        };
    },
    mounted() {
        this.getShiftCov();
    },
    methods: {
        toggleShowModal() {
            this.$parent.toggleShiftCov();
        },
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
                    this.$store.state.globalconstraints[0] = [this.weekly_cover_instance.mon_shift1, this.weekly_cover_instance.mon_shift2, this.weekly_cover_instance.mon_shift3, "Monday"]
                    this.$store.state.globalconstraints[1] = [this.weekly_cover_instance.tue_shift1, this.weekly_cover_instance.tue_shift2, this.weekly_cover_instance.tue_shift3, "Tuesday"]
                    this.$store.state.globalconstraints[2] = [this.weekly_cover_instance.wed_shift1, this.weekly_cover_instance.wed_shift2, this.weekly_cover_instance.wed_shift3, "Wednesday"]
                    this.$store.state.globalconstraints[3] = [this.weekly_cover_instance.thu_shift1, this.weekly_cover_instance.thu_shift2, this.weekly_cover_instance.thu_shift3, "Thursday"]
                    this.$store.state.globalconstraints[4] = [this.weekly_cover_instance.fri_shift1, this.weekly_cover_instance.fri_shift2, this.weekly_cover_instance.fri_shift3, "Friday"]
                    this.$store.state.globalconstraints[5] = [this.weekly_cover_instance.sat_shift1, this.weekly_cover_instance.sat_shift2, this.weekly_cover_instance.sat_shift3, "Saturday"]
                    this.$store.state.globalconstraints[6] = [this.weekly_cover_instance.sun_shift1, this.weekly_cover_instance.sun_shift2, this.weekly_cover_instance.sun_shift3, "Sunday"]
                    this.$parent.toggleShiftCov();
                })
                .catch((error) => {
                    console.log(JSON.stringify(error));
                });
        },
    }
};
</script>

<style scoped>

</style>