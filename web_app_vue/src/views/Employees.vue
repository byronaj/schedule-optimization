<!-- Temporary file for testing purposes -->
<!-- Remember to modify router when this file is deleted -->

<template>
    <div class="container is-fluid">
        <div class="columns is-multiline">
            <div class="column is-full">
                <h1 class="title is-2">Employees</h1>
                <router-link to="@/views/employee-add">Add Employee</router-link>
            </div>

            <hr />

            <div class="column is-full">
                <table class="table is-striped is-hoverable">
                    <thead>
                    <tr>
                        <th class="is-size-6">id</th>
                        <th class="is-size-6">First Name</th>
                        <th class="is-size-6">Last Name</th>
                        <!--<th>FTE</th>
                    <th>Shift</th>
                    <th>Active</th>-->
                        <th></th>
                    </tr>
                    </thead>

                    <tbody>
                    <tr v-for="employee in employees" v-bind:key="employee.id">
                        <td>{{ employee.id }}</td>
                        <td>{{ employee.first_name }}</td>
                        <td>{{ employee.last_name }}</td>
                        <!--<td>{{ employee.fte }}</td>
                    <td>{{ employee.shift_block }}</td>
                    <td>{{ employee.is_active }}</td>-->
                        <td>
                            <router-link :to="{ name: 'EmployeeModify', params: { id: employee.id } }" class="button is-small is-link is-light"> Edit </router-link>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Employees',
    data() {
        return {
            employees: [],
        };
    },
    mounted() {
        this.getEmployees();
    },
    methods: {
        getEmployees() {
            axios
                .get(`/api/v1/employees/`)
                .then((response) => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.employees.push(response.data[i]);
                    }
                })
                .catch((error) => {
                    console.log(JSON.stringify(error));
                });
        },
    },
};
</script>

<style scoped>

</style>