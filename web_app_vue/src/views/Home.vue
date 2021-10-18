<template>
  <div v-if="!$store.state.user.isAuthenticated" class="home">
    <section class="section hero is-medium is-primary is-bold">
      <div class="hero-body">
        <div class="container has-text-centered">
          <p class="title">
            Welcome to Schedule Optimizer
          </p>
          <p class="subtitle">
            An automatic shift scheduler
          </p>
        </div>
      </div>
    </section>
  </div>
  <div v-else-if="$store.state.user.isAuthenticated">
    <Dashboard />
  </div>
</template>

<script>

// @ is an alias to /src
import Dashboard from '@/views/Dashboard'
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
  name: 'Home',
  components: {
    Dashboard
  },
}
</script>

<style>
.home {
  width: 100%;
}
</style>