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
      ["Max hour shifts", 8],
      ["Max consecutive working days", 5],
      ["Min consecutive working days", 2],
      ["Min consecutive free days", 2],
      ["Max consecutive weekends", 2],
      ["Back-to-Back Shifts", false],
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
