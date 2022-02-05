import Vue from "vue";
import VueRouter from "vue-router";

import Login from "@/views/Login.vue"
import Logout from "@/views/Logout.vue"
import Register from "@/views/suppliers/Register.vue"
import NotFound from "@/views/404.vue"

import store from "../store/index"

const routes = [
  {
    path: "*",
    name: "NotFound",
    component: NotFound
  },
  {
    path: "/",
    name: "Login",
    component: Login
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: {
      requiresAuth: true
    }
  }
];


Vue.use(VueRouter);
const router = new VueRouter({
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
  mode: "history",
  routes
});

// router.beforeEach(async (to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (store.getters.isLoggedIn) {
//       next();
//     } else {
//       next("/");
//     }
//   } else {
//     next();
//   }
// });

export default router
