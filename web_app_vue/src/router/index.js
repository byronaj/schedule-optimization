import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
// import HomeAuthenticated from '@/views/HomeAuthenticated'
// import HomeUnauthenticated from '@/views/HomeUnauthenticated'
import Dashboard from '@/views/Dashboard.vue'
import SignUp from '@/views/SignUp.vue'
import LogIn from '@/views/LogIn.vue'

import store from '@/store'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  // {
  //   path: '/home-postauth',
  //   name: 'HomeAuthenticated',
  //   component: HomeAuthenticated,
  //   meta: {
  //     requireLogin: true
  //   }
  // },
  // {
  //   path: '/home-preauth',
  //   name: 'HomeUnauthenticated',
  //   component: HomeUnauthenticated
  // },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {  // DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/employees',
    name: 'Employees',
    component: () => import('../views/Employees.vue'),

  },
  {  // DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/employee-modify',
    name: 'EmployeeModify',
    component: () => import('../views/EmployeeModify.vue'),
  },
  {  // DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/employee-add',
    name: 'EmployeeAdd',
    component: () => import('../views/EmployeeAdd.vue'),
  },
  {  // DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/constraints-avm',
    name: 'ConstraintsAddViewModify',
    component: () => import('../views/ConstraintsAddViewModify.vue'),
  },
  {  // DELETE after API testing is done and code is finished being used to assist in implementing production version
    path: '/coverage-req',
    name: 'ConstraintCoverageModify',
    component: () => import('../views/ConstraintsAddViewModify.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

// For multiple user types
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
