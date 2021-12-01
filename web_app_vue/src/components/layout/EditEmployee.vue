<template>
  <div id="editEmployee">
    <Modal>
      <header class="modal-card-head">
				<p class="modal-card-title">View Employees</p>
				<button class="delete" aria-label="close" @click="toggleShowEditEmployee"></button>
			</header>

      <section class="modal-card-body" style="color: #000">
        <div class="field">
          <div class="column is-12">
            <h1 class="title">Edit — {{ employee.id }}: {{ employee.first_name }} {{ employee.last_name }}</h1>
          </div>

          <div class="column is-6">
            <div class="field">
              <label>First Name</label>

              <div class="control">
                <input type="text" class="input" v-model="employee.first_name" />
              </div>
            </div>

            <div class="field">
              <label>Last Name</label>

              <div class="control">
                <input type="text" class="input" v-model="employee.last_name" />
              </div>
            </div>

            <div class="field">
              <label class="label">FTE</label>

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

            <div class="column is-6">
              <div class="field">
                <label class="label">Active</label>

                <div class="control">
                  <label class="checkbox">
                    <input type="checkbox" v-model="employee.is_active" />
                  </label>
                </div>
              </div>
            </div>
          </div>

          <div class="columns">
            <div class="field is-grouped">
              <div class="control">
                <button class="button is-success" @click="submitForm">
                  <span class="icon"><i class="fas fa-check"></i></span>
                  <span>Save</span>
                </button>
              </div>

              <div class="control">
                <button class="button mgl-small is-outlined" @click="toggleShowEditEmployee">
                  <span>Cancel</span>
                </button>
              </div>

              <div class="control is-right">
                <button class="button is-danger is-outlined" @click="deleteForm">
                  <span>Delete</span>
                  <span class="icon"><i class="fas fa-times"></i></span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </Modal>
  </div>
</template>

<script>
  import axios from 'axios';
	import { toast } from 'bulma-toast';
  import Modal from '@/components/Modal.vue';

	export default {
		name: 'EditEmployee',
    components: { Modal },
    props: { empID: Number },
		data() {
			return {
				employee: {},
			};
		},
		mounted() {
			this.getEmployee();
		},
		methods: {
			getEmployee() {
				const employeeId = this.empID;
				axios
					.get(`/api/v1/employees/${employeeId}`)
					.then((response) => {
						this.employee = response.data;
					})
					.catch((error) => {
						console.log(JSON.stringify(error));
					});
			},
			submitForm() {
				const employeeId = this.empID;
				axios
					.patch(`/api/v1/employees/${employeeId}/`, this.employee)
					.then((response) => {
						toast({
							message: 'Changes saved',
							type: 'is-success',
							dismissible: true,
							pauseOnHover: true,
							duration: 2000,
							position: 'bottom-right',
						});
						this.cancelForm(); //close Modal
					})
					.catch((error) => {
						console.log(JSON.stringify(error));
					});
			},
			cancelForm() {
				this.toggleShowEditEmployee(); //toggle close Modal
			},
			deleteForm() {
				const employeeId = this.empID;
				axios
					.delete(`/api/v1/employees/${employeeId}/`)
					.then((response) => {
						toast({
							message: 'Employee Deleted',
							type: 'is-danger',
							dismissible: true,
							pauseOnHover: true,
							duration: 2000,
							position: 'bottom-right',
						});
						this.cancelForm(); //close Modal
					})
					.catch((error) => {
						console.log(JSON.stringify(error));
					});
			},
      toggleShowEditEmployee() {
				this.$parent.toggleShowEditEmployee(-1); //toggle-close Modal from parent Modal
			},
		},
	};
</script>

<style>

</style>