<template>
	<div
		class="container vh-100 d-flex justify-content-center align-items-center"
	>
		<div class="login col-4 border p-5">
			<h3 class="text-center mb-4">Mada CRM</h3>
			<form @submit.prevent="submitForm">
				<div class="form-group">
					<input
						type="text"
						class="form-control"
						id="username"
						placeholder="Username"
						v-model="username"
					/>
				</div>
				<div class="form-group">
					<input
						type="password"
						class="form-control"
						id="password"
						placeholder="Password"
						v-model="password"
					/>
				</div>
				<span v-show="error" class="error mb-3">Incorrect Credentials</span>
				<button type="submit" class="btn btn-primary float-right">Login</button>
			</form>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'LoginView',
	data() {
		return {
			username: '',
			password: '',
			error: false,
		};
	},
	methods: {
		async submitForm(e) {
			const formData = {
				username: this.username,
				password: this.password,
			};
			try {
				const response = await axios.post('/api/token/login', formData);

				const token = response.data.auth_token;

				this.$store.commit('setToken', token);

				axios.defaults.headers.common['Authorization'] = 'Token ' + token;

				localStorage.setItem('token', token);
				this.$router.push('/');
			} catch (e) {
				this.error = true;
			}
		},
	},
};
</script>

<style scoped>
.login {
	background-color: white;
}
.error {
	display: block;
	color: red;
}
</style>
