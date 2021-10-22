<template>
  <div class="hero-head">
    <nav class="navbar is-dark has-shadow" role="navigation" aria-label="main navigation" style="min-height: 4rem;">
      <div class="container">

        <div class="navbar-brand">

          <a class="navbar-item is-size-4" href="/">
            <img src="@/assets/calendar_128px.png" alt="calendar logo">
            Schedule Optimizer
          </a>

          <span class="navbar-burger">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </div>

        <div id="navbar" class="navbar-menu">

          <div class="navbar-start">
            <template v-if="$store.state.user.isAuthenticated">
              <a class="navbar-item" v-on:click="showModal = true">
                Add Employee
              </a>
              <modal v-if="showModal" v-on:close="showModal = false">

                <header class="modal-card-head">
                  <p class="modal-card-title">
                    Add Employee
                  </p>
                  <button class="delete" aria-label="close" v-on:click="showModal = false"></button>
                </header>

                <section class="modal-card-body">
                  <div class="field">
                    <label class="label">
                      First Name
                    </label>
                    <div class="control">
                      <input class="input" type="text">
                    </div>
                  </div>

                  <div class="field">
                    <label class="label">
                      Last Name
                    </label>
                    <div class="control">
                      <input class="input" type="text">
                    </div>
                  </div>
                </section>

                <footer class="modal-card-foot">
                  <button class="button is-success">
                    Save changes
                  </button>
                  <button class="button" aria-label="close" v-on:click="showModal = false">
                    Cancel
                  </button>
                </footer>

              </modal>
            </template>
            <a class="navbar-item" @click="toggleEditConstraints">
                Edit Constraints
            </a>
            <div v-if="showEditConstraints">
              <EditConstraints />
            </div>
          </div>

          <div class="navbar-end">
            <a href="/about" class="navbar-item">About</a>
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
    toggleEditConstraints() {
      this.showEditConstraints = !this.showEditConstraints
    }
  },
  name: 'Nav',
  components: {
    Modal, EditConstraints
  },
  data() {
    return {
      showModal: false,
      showEditConstraints: false,
    }
  }
}
</script>

<style scoped>

</style>
