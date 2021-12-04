import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      id: 0,
      username: '',
    },
    isAuthenticated: false,
    token: '',
    globalconstraints: [
      [0, 0, 0, "Monday"],
      [0, 0, 0, "Tuesday"],
      [0, 0, 0, "Wednesday"],
      [0, 0, 0, "Thursday"],
      [0, 0, 0, "Friday"],
      [0, 0, 0, "Saturday"],
      [0, 0, 0, "Sunday"],
    ],
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.user.token = localStorage.getItem('token')
        state.user.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')
      } else {
        state.user.id = ''
        state.user.username = ''
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token) {
      state.user.token = token
      state.user.isAuthenticated = true
    },
    removeToken(state) {
      state.user.id = ''
      state.user.username = ''
      state.user.token = ''
      state.user.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
  },
  actions: {
  },
  modules: {
  }
})
