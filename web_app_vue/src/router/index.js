import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
// import { authenticationGuard } from "@/auth/authentication-guard";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/About.vue')
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
  // {
  //   path: '/dashboard',
  //   name: 'Dashboard',
  //   component: () => import('../views/Dashboard.vue'),
  //   beforeEnter: authenticationGuard
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
