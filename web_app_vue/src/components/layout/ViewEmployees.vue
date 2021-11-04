<template>
    <div id="viewemployees">
    <Modal v-on:close="toggleShowViewEmployees">
        <header class="modal-card-head">
            <p class="modal-card-title">
            View Employees
            </p>
            <button class="delete" aria-label="close" @click="toggleShowViewEmployees"></button>
        </header>

        <section class="modal-card-body" style="color:black;">
            <div class="field">
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
        </section>
    </Modal>
    </div>
</template>

<script>
import axios from 'axios'
import Modal from "@/components/Modal.vue";

export default {
  name: "ViewEmployees",
  components: { Modal },
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
    },
    toggleShowViewEmployees() {
          this.$parent.toggleViewEmployees()
    },
  }
}
</script>

<style>
#viewemployees .modal-card {
  width: 90%;
}
</style>