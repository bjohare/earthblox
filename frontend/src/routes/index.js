import Vue from "vue";
import VueRouter from "vue-router";

import Login from "@/views/users/Login.vue"
import Logout from "@/views/users/Logout.vue"
import NotFound from "@/views/404.vue"

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

export default router
