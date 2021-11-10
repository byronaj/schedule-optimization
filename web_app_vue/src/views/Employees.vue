<!-- Temporary file for testing purposes -->
<!-- Remember to modify router when this file is deleted -->

<template>
  <div class="container">

    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Employees</h1>
          <router-link to="@/views/add">Add Employee</router-link>
      </div>

      <hr>

    <div class="column is-boxed">
      <table class="table is-fullwidth">
        <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>FTE</th>
          <th>Shift</th>
          <th>Active</th>
          <th></th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="employee in employees" v-bind:key="employee.id">
          <td>{{ employee.first_name }}</td>
          <td>{{ employee.last_name }}</td>
          <td>{{ employee.fte }}</td>
          <td>{{ employee.shift_block }}</td>
          <td>{{ employee.is_active }}</td>
          <td>
            <router-link :to="{ name: 'EditEmployee', params: { id: employee.id }}" class="button is-info">Edit</router-link>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    </div>
  </div>
 </template>

<script>
import axios from 'axios'

export default {
  name: "Employees",
  data() {
    return {
      employees: []
    }
  },
  mounted() {
    this.getEmployees()
  },
  methods: {
    getEmployees() {
      axios
          .get(`/api/v1/employees/`)
          .then(response => {
            for (let i = 0; i < response.data.length; i++) {
              this.employees.push(response.data[i])
            }
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })
    }
  }
}

</script>

<style scoped>

</style>