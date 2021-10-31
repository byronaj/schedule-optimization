import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

import store from '@/store'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: () => import('../views/LogIn.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/Dashboard.vue'),
    meta: {
      requireLogin: true
    }
  },
  { // DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/employees',
    name: 'Employees',
    component: () => import('../views/Employees.vue'),

  },
  { /// DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/add',
    name: 'Add',
    component: () => import('../views/Add.vue'),

  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

// Probably not going to do multiple user types (or perhaps just do it half-assed)
// router.beforeEach(async (to, from) => {
//   // canUserAccess() returns `true` or `false`
//   const canAccess = await canUserAccess(to)
//   if (!canAccess) return '/login'
// })

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
