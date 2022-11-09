<template>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
		<router-link to="/" class="brand">Mada CRM</router-link>
		<div class="ml-auto">
			<span class="user mr-5">Welcome, {{ user }}</span>
			<button @click="logout" class="btn btn-light">Logout</button>
		</div>
	</nav>
</template>

<script>
import axios from 'axios';

export default {
	name: 'LayoutComponent',
	data() {
		return {
			user: '',
		};
	},
	methods: {
		async logout() {
			const response = await axios.post('/api/token/logout');
			
			localStorage.removeItem('token');

			this.$store.commit('removeToken');

			axios.defaults.headers.common['Authorization'] = '';

			this.$router.push('/login');
		},
	},
	async beforeCreate() {
		const response = await axios.get('/api/users/me');
		this.user = response.data.username;
	},
};
</script>

<style scoped>
.brand {
	font-size: 20px;
	font-weight: 700;
	text-decoration: none;
	color: white;
}
.user {
	color: white;
}
</style>
