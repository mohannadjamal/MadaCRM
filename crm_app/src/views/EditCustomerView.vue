<template>
	<LayoutComponent />
	<div class="container d-flex flex-column align-items-center">
		<h3 class="mt-5">Edit Customer</h3>
		<span v-if="error" class="error mb-3">{{ error }}</span>
		<form @submit.prevent="submit" class="col-4">
			<div class="form-group">
				<label for="firstname">First Name:</label>
				<input
					type="text"
					class="form-control"
					id="firstname"
					placeholder="Enter first name"
					v-model="firstname"
				/>
			</div>
			<div class="form-group">
				<label for="lastname">Last Name:</label>
				<input
					type="text"
					class="form-control"
					id="lastname"
					placeholder="Enter last name"
					v-model="lastname"
				/>
			</div>
			<div class="form-group">
				<label for="phone">Phone:</label>
				<input
					type="text"
					class="form-control"
					id="phone"
					placeholder="Enter phone number"
					v-model="phone"
				/>
			</div>
			<div class="form-group">
				<label for="services">Select Services</label>
				<button
					type="button"
					class="btn btn-success float-right mb-2"
					@click="addService"
				>
					+
				</button>
				<select class="form-control" id="services" v-model="service">
					<option v-for="service in services">
						{{ service.name }}
					</option>
				</select>
			</div>
			<div class="py-2 d-flex justify-content-between">
				<h5>Added services</h5>
			</div>
			<table class="table">
				<thead>
					<tr>
						<th scope="col">#</th>
						<th scope="col">Name</th>
						<th scope="col">Description</th>
						<th scope="col">Actions</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="service in selectedServices">
						<th scope="row">{{ service.id }}</th>
						<td>{{ service.name }}</td>
						<td>{{ service.description }}</td>
						<td>
							<button
								class="action btn btn-danger"
								type="button"
								@click="() => removeService(service)"
							>
								Remove
							</button>
						</td>
					</tr>
				</tbody>
			</table>
			<button type="submit" class="btn btn-primary float-right">
				Edit Customer
			</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';
import LayoutComponent from '@/components/LayoutComponent.vue';

export default {
	name: 'AddCustomerView',
	components: {
		LayoutComponent,
	},
	data() {
		return {
			firstname: '',
			lastname: '',
			phone: '',
			service: '',
			services: [],
			selectedServices: [],
			error: '',
		};
	},
	async beforeCreate() {
		const response = await axios.get('/api/services/');

		const responseCustomer = await axios.get(
			`/api/customers/${this.$route.params.id}/`
		);
		this.firstname = responseCustomer.data.firstname;
		this.lastname = responseCustomer.data.lastname;
		this.phone = responseCustomer.data.phone;
		this.selectedServices = responseCustomer.data.services;

		this.services = response.data.filter(
			(service) =>
				!this.selectedServices.find(
					(selectedService) => service.id === selectedService.id
				)
		);
	},
	methods: {
		addService() {
			if (this.service) {
				const selectedService = this.services.find(
					(service) => service.name === this.service
				);
				this.services = this.services.filter(
					(service) => service.id !== selectedService.id
				);
				this.selectedServices = [...this.selectedServices, selectedService];
			}
		},
		removeService(service) {
			this.services = [...this.services, service];
			this.selectedServices = this.selectedServices.filter(
				(item) => item.id !== service.id
			);
		},
		async submit(e) {
			if (this.firstname && this.lastname && this.phone) {
				const formData = {
					firstname: this.firstname,
					lastname: this.lastname,
					phone: this.phone,
					services: this.selectedServices,
				};
				console.log(formData)
				try {
					const response = await axios.put(
						`/api/customers/${this.$route.params.id}/`,
						formData
					);
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
.table {
	background-color: white;
}
.error {
	display: block;
	color: red;
}
</style>
