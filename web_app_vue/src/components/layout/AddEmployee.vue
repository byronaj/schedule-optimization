<template>
    <Modal v-on:close="toggleShowModal">
        <header class="modal-card-head">
            <p class="modal-card-title">Add Employee</p>
            <button class="delete" aria-label="close" @click="toggleShowModal"></button>
        </header>

        <section class="modal-card-body">
            <div class="field">
                <label class="label">First Name</label>

                <div class="control">
                    <input class="input is-info" type="text" v-model="employee.first_name" placeholder="First" />
                </div>
            </div>

            <div class="field">
                <label class="label">Last Name</label>

                <div class="control">
                    <input class="input is-info" type="text" v-model="employee.last_name" placeholder="Last" />
                </div>
            </div>

            <div class="field">
                <label class="label">FTE Hours Allocated</label>

                <div class="control">
                    <div class="select is-info">
                        <select v-model="employee.fte">
                            <option value="1.0">1.0</option>
                            <option value="0.9">0.9</option>
                            <option value="0.8">0.8</option>
                            <option value="0.7">0.7</option>
                            <option value="0.6">0.6</option>
                            <option value="0.5">0.5</option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="field">
                <label class="label">Shift</label>

                <div class="control">
                    <div class="select is-info">
                        <select v-model="employee.shift_block">
                            <option value="0">Variable</option>
                            <option value="1">First</option>
                            <option value="2">Second</option>
                            <option value="3">Third</option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="field">
                <label class="label">Active</label>

                <div class="control">
                    <label class="checkbox">
                        <input type="checkbox" v-model="employee.is_active" />
                    </label>
                </div>
            </div>
        </section>

        <footer class="modal-card-foot">
            <button class="button is-success" @click="submitForm">Save changes</button>
            <button class="button" aria-label="close" @click="toggleShowModal">Cancel</button>
        </footer>
    </Modal>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import Modal from '@/components/Modal';

export default {
    name: 'AddEmployee',
    components: { Modal },
    data() {
        return {
            showModal: false,
            employee: {},
        };
    },
    methods: {
        toggleShowModal() {
            this.$parent.toggleAddEmployee();
        },
        submitForm() {
            axios
                .post(`/api/v1/employees/`, this.employee)

                .then((response) => {
                    toast({
                        message: 'The employee was added.',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    });
                    this.$parent.toggleAddEmployee();
                })

                .catch((error) => {
                    console.log(JSON.stringify(error));
                });
        },
    },
};
</script>

<style scoped></style>
