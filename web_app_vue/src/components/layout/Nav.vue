<template>
    <div class="hero-head">
        <nav aria-label="main navigation" class="navbar is-dark has-shadow" role="navigation" style="min-height: 4rem">
            <div class="container">
                <div class="navbar-brand">
                    <img alt="calendar logo" class="is-static" href="#" src="@/assets/icon.png" />
                    <a class="navbar-item is-size-5 has-text-grey-light" href="/">schedule optimizer</a>

                    <a aria-expanded="false" aria-label="menu" class="navbar-burger" role="button">
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                    </a>
                </div>

                <div id="navbar" class="navbar-menu">
                    <div class="navbar-start">
                        <template v-if="$store.state.user.isAuthenticated">

                            <!-- Employee Maintenance Dropdown Menu -->
                            <div class="navbar-item has-dropdown is-hoverable">
                                <a class="navbar-link">Employee Maintenance</a>
                                <div class="navbar-dropdown has-background-light">
                                    <a class="navbar-item has-text-primary-dark" @click="toggleAddEmployee">Add Employee</a>
                                    <a class="navbar-item has-text-info-dark" @click="toggleViewEmployees">View/Modify Employees</a>
                                </div>
                            </div>

                            <div v-if="showAddEmployee">
                                <AddEmployee />
                            </div>

                            <div v-if="showViewEmployees">
                                <ViewEmployees />
                            </div>

                            <!-- Constraint Maintenance -->
                            <a class="navbar-item" @click="toggleShiftCov">
                                Shift Coverage
                            </a>
                            <router-link class="navbar-item" to="/constraints-avm">
                                Scheduling Constraints
                            </router-link>

<!--                            <div class="navbar-item has-dropdown is-hoverable">-->
<!--                                <a class="navbar-link">Scheduling Options</a>-->
<!--                                <div class="navbar-dropdown has-background-light">-->
<!--                                    <a class="navbar-item has-text-primary-dark" @click="toggleShiftCov">-->
<!--                                        Shift Coverage-->
<!--                                    </a>-->
<!--                                    <a class="navbar-item" @click="toggleEditConstraints">-->
<!--                                        Scheduling Constraints-->
<!--                                    </a>-->
<!--                                    <a class="navbar-item has-text-info-dark" @click="">Shift Transitions</a>-->
<!--                                    <a class="navbar-item has-text-info-dark" @click="">Continuous Sequence</a>-->
<!--                                    <a class="navbar-item has-text-info-dark" @click="">Weekly Sums</a>-->
<!--                                </div>-->
<!--                            </div>-->

                            <div v-if="showShiftCov">
                                <ShiftCoverage />
                            </div>

                        </template>
                    </div>

                    <div class="navbar-end">
                        <div class="navbar-item is-active">
                            <div class="buttons">
                                <template v-if="$store.state.user.isAuthenticated">
                                    <router-link class="button is-danger is-outlined" to="/" @click="logout()">
                                        <strong>Log out</strong>
                                    </router-link>
                                </template>

                                <template v-else>
                                    <router-link class="button is-info is-outlined" to="/sign-up">
                                        <strong>Sign up</strong>
                                    </router-link>

                                    <router-link class="button is-primary is-outlined" to="/log-in">
                                        <strong>Log in</strong>
                                    </router-link>
                                </template>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import axios from 'axios';

import Modal from '@/components/Modal.vue';
import EditConstraints from '@/components/layout/EditConstraints.vue';
import AddEmployee from '@/components/layout/AddEmployee.vue';
import ViewEmployees from '@/components/layout/ViewEmployees.vue';
import ShiftCoverage from '@/components/layout/ShiftCoverage.vue';
import ConstraintsAddViewModify from "@/views/ConstraintsAddViewModify";

export default {
    name: 'Nav',
    components: {
        ConstraintsAddViewModify,
        Modal,
        AddEmployee,
        EditConstraints,
        ViewEmployees,
        ShiftCoverage,
    },
    data() {
        return {
            showEditConstraints: false,
            showAddEmployee: false,
            showViewEmployees: false,
            showShiftCov: false,
            userType: localStorage.getItem('userType'),
        };
    },
    methods: {
        logout() {
            console.log('logout');
            axios.defaults.headers.common['Authorization'] = '';
            localStorage.removeItem('token');
            this.$store.commit('removeToken');
            this.$router.push('/');
        },
        toggleAddEmployee() {
            this.showAddEmployee = !this.showAddEmployee;
        },
        toggleEditConstraints() {
            this.showEditConstraints = !this.showEditConstraints;
        },
        toggleViewEmployees() {
            this.showViewEmployees = !this.showViewEmployees;
        },
        toggleShiftCov() {
            this.showShiftCov = !this.showShiftCov
        },
    },
};
</script>

<style scoped></style>