import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseUrl = 'http://127.0.0.1:8000'

createApp(App).use(store).use(router, axios).mount('#app')


import { dom } from '../node_modules/@fortawesome/fontawesome-svg-core'
dom.watch()

import { library } from '../node_modules/@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '../node_modules/@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '../node_modules/@fortawesome/vue-fontawesome'

library.add(faUserSecret)
Vue.component('font-awesome-icon', FontAwesomeIcon)
