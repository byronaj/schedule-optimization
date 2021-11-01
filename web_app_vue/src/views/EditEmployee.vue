<!-- Temporary file for testing purposes -->
<!-- Remember to modify router when this file is deleted -->

<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit - {{ employee.first_name }} {{ employee.last_name }}</h1>
      </div>

      <div class="column is-6">
        <div class="field">
          <label>First Name</label>

          <div class="control">
            <input type="text" class="input" v-model="employee.first_name">
          </div>
        </div>

        <div class="field">
          <label>Last Name</label>

          <div class="control">
            <input type="text" class="input" v-model="employee.last_name">
          </div>
        </div>

        <div class="field">
          <label class="label">
            FTE
          </label>
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
        <label class="label">
          Shift
        </label>
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

        <div class="column is-6">
        <div class="field">
        <label class="label">
          Active
        </label>
        <div class="control">
          <label class="checkbox">
            <input type="checkbox"  v-model="employee.is_active">
          </label>
        </div>
      </div>
      </div>

        <div class="column is-12">
          <div class="field">
            <div class="control">
              <button class="button is-success" @click="submitForm">Save changes</button>
            </div>
          </div>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from "bulma-toast";

export default {
  name: "EditEmployee",
  data() {
    return {
        employee: {}
    }
  },
  mounted() {
    this.getEmployee()
  },
  methods: {
    getEmployee() {
      const employeeId = this.$route.params.id
      axios
          .get(`/api/v1/employees/${employeeId}`)
          .then(response => {
            this.employee = response.data
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })
    },
    submitForm() {
      const employeeId = this.$route.params.id
      axios
          .patch(`/api/v1/employees/${employeeId}/`, this.employee)
          .then(response => {
            toast({
              message: 'Changes saved',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
              this.$router.push('/employees')
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