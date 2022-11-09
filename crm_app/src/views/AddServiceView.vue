<template>
	<LayoutComponent />
	<div class="container d-flex flex-column align-items-center">
		<h3 class="mt-5">Add A Service</h3>
		<span v-if="error" class="error mb-3">{{ error }}</span>
		<form @submit.prevent="submit" class="col-4">
			<div class="form-group">
				<label for="firstname">Name:</label>
				<input
					type="text"
					class="form-control"
					id="firstname"
					placeholder="Enter name"
					v-model="name"
				/>
			</div>
			<div class="form-group">
				<label for="lastname">Description:</label>
				<input
					type="text"
					class="form-control"
					id="lastname"
					placeholder="Enter last name"
					v-model="description"
				/>
			</div>
			<button type="submit" class="btn btn-primary float-right">
				Add Service
			</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';
import LayoutComponent from '@/components/LayoutComponent.vue';

export default {
	name: 'AddServiceView',
	components: {
		LayoutComponent,
	},
	data() {
		return {
			name: '',
			description: '',
			error: '',
		};
	},

	methods: {
		async submit(e) {
			if (this.name && this.description) {
				const formData = {
					name: this.name,
					description: this.description,
				};
				try {
					const response = await axios.post('/api/services/', formData);
					this.$router.push('/');
				} catch (e) {
					this.error = 'Something went wrong';
				}
			} else {
				this.error = 'Please check the fields if empty';
			}
		},
	},
};
</script>

<style scoped>
.error {
	display: block;
	color: red;
}
</style>
