<template>
  <div class="about">
    <div class="hero is-primary is-bold">
      <div class="hero-body has-text-centered">
        <h1 class="title">Log in</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">

            <form v-on:submit.prevent="submitForm">

              <div class="field">
                <label>Email</label>
                <div class="control">
                  <input type="email" class="input" v-model="username">
                </div>
              </div>

              <div class="field">
                <label>Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password">
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-dark">Log in</button>
                </div>
              </div>
            </form>

            <hr>

            Or
            <router-link to="/sign-up">click here</router-link>
            to sign up
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async submitForm(e) {
      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem('token')

      const formData = {
        username: this.username,
        password: this.password
      }

      await axios
          .post('/api/v1/token/login/', formData)

          .then(response => {
            const token = response.data.auth_token
            //const userType = response.data.userType
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = "Token " + token
            localStorage.setItem('token', token)
            // localStorage.setItem('userType', 0) //for testing
          })

          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push(JSON.stringify(error.message))
            } else {
              console.log(JSON.stringify(error))
            }
          })

      axios
          .get('/api/v1/users/me')

          .then(response => {
            this.$store.commit('setUser', {'username': response.data.username, 'id': response.data.id})
            localStorage.setItem('username', response.data.username)
            localStorage.setItem('userid', response.data.id)
            this.$router.push('/')
          })

          .catch(error => {
            console.log(JSON.stringify(error))
          })

    }
  }
}
</script>