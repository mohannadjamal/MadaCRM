<template>
	<!--<nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>-->
	<router-view />
</template>

<script>
import axios from 'axios';

export default {
	name: 'App',
	beforeCreate() {
		this.$store.commit('initializeStore');

		const token = this.$store.state.token;

		if (token) {
			axios.defaults.headers.common['Authorization'] = 'Token ' + token;
		} else {
			axios.defaults.headers.common['Authorization'] = null;
		}
	},
};
</script>
<style>
:root {
	background-color: #f7f7f7;
}
#app {
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	background-color: #f7f7f7;
}
</style>
