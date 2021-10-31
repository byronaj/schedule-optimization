<template>
  <div class="signup">
    <div class="hero is-primary is-bold">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign Up</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">

            <form v-on:submit.prevent="submitForm">
              <div class="field">
                <label>Email</label>
                <input class="input" type="email" v-model="username">
              </div>

              <div class="field">
                <label>Password</label>
                <div class="control">
                  <input class="input" type="password" v-model="password">
                </div>
              </div>

              <div class="field">
                <label>Repeat password</label>
                <div class="control">
                  <input class="input" type="password" v-model="password2">
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>

              <div class="field">
                <div class="control">
                  <button class="button is-dark">Sign up</button>
                </div>
              </div>
            </form>

            <hr>

            Or
            <router-link to="/log-in">click here</router-link>
            to log in

          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

import { toast } from 'bulma-toast'

export default {
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password
    }
    axios
      .post('/api/v1/users/', formData)
      .then(response => {
        console.log(response)
        toast({
          message: 'Account was created successfully. Please log in.',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        this.$router.push('/log-in')
      })
      .catch(error => {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
          console.log(JSON.stringify(error.response.data))
        } else if (error.message) {
          console.log(JSON.stringify(error.message))
        } else {
          console.log(JSON.stringify(error))
        }
      })
    }
  }
}
</script>