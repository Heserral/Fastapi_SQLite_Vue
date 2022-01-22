//https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/#handling-unauthorized-users-and-expired-tokens

//npm install --save axios@0.21.1 vuex@3.6.2 vuex-persistedstate@4.0.0 bootstrap@5.1.0

import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/'; 

Vue.config.productionTip = false

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      store.dispatch('logOut');
      return router.push('/login')
    }
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
