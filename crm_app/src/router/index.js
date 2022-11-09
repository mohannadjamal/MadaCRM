import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import AddCustomerView from '@/views/AddCustomerView.vue';
import AddServiceView from '@/views/AddServiceView.vue';
import EditCustomerView from '@/views/EditCustomerView.vue'
import store from '@/store';
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/addcustomer',
    name: 'addcustomer',
    component: AddCustomerView
  },
  {
    path: '/addservice',
    name: 'addservice',
    component: AddServiceView
  },
  {
    path: '/editcustomer/:id',
    name: 'editcustomer',
    component: EditCustomerView
  }
  //{
  //  path: '/about',
  //  name: 'about',
  //  // route level code-splitting
  //  // this generates a separate chunk (about.[hash].js) for this route
  //  // which is lazy-loaded when the route is visited.
  //  component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  //}
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach(async (to, from) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const isAuthenticated = store.state.isAuthenticated;

  if (authRequired && !isAuthenticated)
    return '/login';

  if (!authRequired && isAuthenticated)
    return from.path;
});
export default router;
