<template>
  <div class="hero-head">
    <nav class="navbar is-dark has-shadow" role="navigation" aria-label="main navigation" style="min-height: 4rem;">
      <div class="container">

        <div class="navbar-brand">
          <img class="is-static" src="@/assets/icon.png" alt="calendar logo" href="#">
          <a class="navbar-item is-size-5" href="/">
            Schedule Optimizer
          </a>

          <a role="button" class="navbar-burger"  aria-label="menu" aria-expanded="false">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbar" class="navbar-menu">
          <div class="navbar-start">

            <template v-if="$store.state.user.isAuthenticated">
              <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link">
                  Employee Maintenance
                </a>
                <div class="navbar-dropdown">
                  <div class="navbar-item" @click="toggleAddEmployee">
                    Add Employee
                  </div>
                  <div class="navbar-item">
                    View/Modify Employees
                  </div>
                </div>
                <div v-if="showAddEmployee">
                    <AddEmployee />
                  </div>
              </div>

              <a class="navbar-item" @click="toggleEditConstraints" v-if="userType==0">
                Edit Constraints
              </a>
              <div v-if="showEditConstraints">
                <EditConstraints />
              </div>
            </template>

          </div>

          <div class="navbar-end">
            <div class="navbar-item is-active">

              <div class="buttons">
                <template v-if="$store.state.user.isAuthenticated">
                  <router-link to="/home" class="button is-danger is-outlined" @click="logout()">
                    <strong>Log out</strong>
                  </router-link>
                </template>
                <template v-else>
                  <router-link to="/sign-up" class="button is-info is-inverted">
                    Sign up
                  </router-link>
                  <router-link to="/log-in" class="button is-primary is-inverted">
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
import axios from "axios";
import Modal from "@/components/Modal.vue";
import EditConstraints from "@/components/layout/EditConstraints.vue"
import AddEmployee from "@/components/layout/AddEmployee";

export default {
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    logout() {
      console.log('logout')

      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem('token')

      this.$store.commit('removeToken')

      this.$router.push('/')
    },
    toggleAddEmployee() {
      this.showAddEmployee = !this.showAddEmployee
    },
    toggleEditConstraints() {
      this.showEditConstraints = !this.showEditConstraints
    },
  },
  name: 'Nav',
  components: {
    Modal,
    AddEmployee,
    EditConstraints,
  },
  data() {
    return {
      showEditConstraints: false,
      showAddEmployee: false,
      userType: localStorage.getItem("userType")
    }
  }
}
</script>

<style scoped>

</style>
