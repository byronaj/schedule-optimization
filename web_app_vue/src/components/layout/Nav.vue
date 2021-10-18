<template>
  <div class="hero-head">
    <nav class="navbar is-dark has-shadow" role="navigation" aria-label="main navigation" style="min-height: 4rem;">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item">
            <img src="@/assets/calendar_128px.png" alt="calendar logo">
          </a>
          <a class="navbar-item is-size-4" href="/">
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
            <a href="/" class="navbar-item">Home</a>
            <a href="/about" class="navbar-item">About</a>
          </div>

          <div class="navbar-end">
            <div class="navbar-item is-active">
              <div class="buttons">
                <template v-if="$store.state.user.isAuthenticated">
                  <router-link to="/home" class="button is-danger is-inverted" @click="logout()">
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

      this.$router.push('/home')
    }
  },
  name: 'Nav'
}
</script>