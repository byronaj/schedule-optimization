<!-- Temporary file for testing purposes -->
<!-- Remember to modify router when this file is deleted -->

<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Employees</h1>
        <template v-if="$store.state.user.isAuthenticated">
          <router-link to="@/views/add">Add Employee</router-link>
        </template>
      </div>

      <hr>

      <form @submit.prevent="getEmployees">
        <div class="field has-addons">
          <div class="control">
              <input type="text" class="input" v-model="query">
          </div>
          <div class="control">
              <button class="button is-success">Search</button>
          </div>
        </div>
      </form>

    </div>

    <div class="column is-12">
      <table class="table is-fullwidth">
        <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>FTE</th>
          <th>Shift</th>
          <th>Active</th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="employee in employees" v-bind:key="employee.id">
          <td>{{ employees.first_name }}</td>
          <td>{{ employees.last_name }}</td>
          <td>{{ employees.fte }}</td>
          <td>{{ employees.shift_block }}</td>
          <td>{{ employees.is_active }}</td>
        </tr>
        </tbody>

      </table>
    </div>
  </div>
 </template>

<script>
import axios from 'axios'

import Add from '@/views/Add.vue'

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
        .get('/api/v1/employees/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.clients.push(response.data[i])
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