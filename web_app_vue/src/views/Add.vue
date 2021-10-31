<!-- Temporary file for testing purposes -->
<!-- Remember to modify router when this file is deleted -->

<template>
  <div class="container">

<!--    Adapt to modal     -->
    <header>
      <p>Add Employee</p>
    </header>
    <template v-if="$store.state.user.isAuthenticated">
    <form>

      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Name</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control">
              <input class="input is-info" type="text" v-model="employee.first_name" placeholder="First">
            </p>
          </div>

          <div class="field">
            <p class="control">
              <input class="input is-info" type="text" v-model="employee.last_name" placeholder="Last">
            </p>
          </div>
        </div>
      </div>


      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">FTE Hours Allocated</label>
        </div>
        <div class="field-body">
          <div class="field">
            <div class="control">
              <div class="select is-info">
                <select v-model="employee.fte">
                  <option value="1.0">1.0</option>
                  <option value="0.9">0.9</option>
                  <option value="0.8">0.8</option>
                  <option value="0.7">0.7</option>
                  <option value="0.6">0.6</option>
                  <option value="0.5">0.5</option>
                  <option value="0.4">0.4</option>
                  <option value="0.3">0.3</option>
                  <option value="0.2">0.2</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Shift</label>
        </div>
        <div class="field-body">
          <div class="field">
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
        </div>
      </div>

      <div class="field is-horizontal">
        <div class="field-label">
          <label class="label">Currently active?</label>
        </div>
        <div class="field-body">
          <div class="field is-narrow">
            <div class="control">
              <label class="checkbox">
                <input type="checkbox"  v-model="employee.is_active">
              </label>
            </div>
          </div>
        </div>
      </div>

      <div class="field is-horizontal">
        <div class="field-label">
          <!-- Left empty for spacing -->
        </div>
        <div class="field-body">

          <div class="field is-grouped">
            <div class="control">
              <button class="button is-primary is-outlined" @click="submitForm">Save changes</button>
            </div>
<!--            <div class="control">-->
<!--              <button class="button is-danger is-outlined" aria-label="close">Cancel</button>-->
<!--            </div>-->
          </div>

        </div>
      </div>

    </form>
    </template>

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: "Add",
  data() {
    return {
      employee: {}
    }
  },
  methods: {
    submitForm() {
      axios
        .post('/api/v1/employees/', this.employee)

        .then(response => {
          toast({
            message: 'The employee was added.',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })
        this.$router.push('/')
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