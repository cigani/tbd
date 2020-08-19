import Vue from 'vue'
import Router from 'vue-router'

import UserAuth from "@/components/UserComponenets/UserAuth";
import UserCreate from "@/components/UserComponenets/UserCreate";

import store from "@/store/store";
import UserView from "@/components/UserComponenets/UserView";
import FlavorView from "@/components/FlavorComponents/FlavorView";

const routes = [
  {
    path: "/users",
    name: "users",
    component: UserView
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
  },
  {
    path: "/flavors",
    name: "flavors",
    component: FlavorView
  }
]

Vue.use(Router)
const router = new Router({
  scrollBehavior(to, from, savedPosition) {
    return {x: 0, y: 0}
  },
  mode: 'history',
  routes,
  store

})

// router.beforeEach((to, from, next) => {
//   if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
//     next()
//   } else {
//     next('/auth')
//   }
// })

export default router
