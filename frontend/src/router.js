import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import UserAuth from "@/components/UserAuth";
import UserCreate from "@/components/UserCreate/UserCreate";
const routes = [
  {path: "/index", name: "index", component: Index},
  {
    path: "/users",
    name: "users",
    component: () => import("./components/UserView")
  },
  {
    path: "/auth",
    name: "auth",
    component: UserAuth
  },
  {
    path: "/create",
    name: "create",
    component: UserCreate,
  }
]


Vue.use(Router)
const router = new Router({
  scrollBehavior(to, from, savedPosition) {
    return {x: 0, y: 0}
  },
  mode: 'history',
  routes

})

// router.beforeEach((to, from, next) => {
//   if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
//     next()
//   } else {
//     next('/auth')
//   }
// })

export default router
