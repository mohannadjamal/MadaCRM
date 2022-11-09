<template>
	<LayoutComponent />
	<div class="container-fluid d-flex flex-column align-items-center">
		<div class="col-10">
			<div class="py-5 d-flex justify-content-between">
				<h4>Customers List</h4>
				<form @submit.prevent="search" class="d-flex flex-row">
					<input type="text" class="form-control" v-model="searchInput" />
					<button class="btn btn-primary ml-2" type="submit">Search</button>
					<button
						class="btn btn-success ml-2"
						@click="addCustomer"
						type="button"
					>
						Add
					</button>
					<button
						v-show="reset"
						class="btn btn-danger ml-2"
						@click="resetSearch"
						type="button"
					>
						Reset
					</button>
				</form>
			</div>
			<table class="table">
				<thead>
					<tr>
						<th scope="col">First Name</th>
						<th scope="col">Last Name</th>
						<th scope="col">Phone</th>
						<th scope="col">Services</th>
						<th scope="col">Actions</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="customer in customers">
						<td>{{ customer.firstname }}</td>
						<td>{{ customer.lastname }}</td>
						<td>{{ customer.phone }}</td>
						<td v-if="customer.services.length > 0">
							<span v-for="(service, index) in customer.services">
								{{ service.name
								}}<span v-if="index !== customer.services.length - 1">, </span>
							</span>
						</td>
						<td v-if="customer.services.length === 0">No Services</td>
						<td>
							<button
								class="action btn btn-warning mr-2"
								@click="() => editCustomer(customer.id)"
								type="button"
							>
								Edit
							</button>
							<button
								class="action btn btn-danger"
								@click="() => deleteCustomer(customer.id)"
								type="button"
							>
								Delete
							</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="col-10">
			<div class="py-5 d-flex justify-content-between">
				<h4>Services List</h4>
				<form class="d-flex flex-row">
					<button
						class="btn btn-success mr-2"
						type="button"
						@click="addService"
					>
						Add
					</button>
				</form>
			</div>
			<table class="table">
				<thead>
					<tr>
						<th scope="col">Name</th>
						<th scope="col">Description</th>
						<th scope="col">Actions</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="service in services">
						<td>{{ service.name }}</td>
						<td>{{ service.description }}</td>
						<td>
							<button
								type="button"
								class="action btn btn-danger"
								@click="() => deleteService(service.id)"
							>
								Delete
							</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import LayoutComponent from '@/components/LayoutComponent.vue';

export default {
	name: 'HomeView',
	components: {
		LayoutComponent,
	},
	data() {
		return {
			customers: [],
			services: [],
			searchInput: '',
			reset: false,
		};
	},
	async beforeCreate() {
		const responseCustomers = await axios.get('/api/customers/');
		this.customers = responseCustomers.data;

		const responseServices = await axios.get('/api/services/');
		this.services = responseServices.data;
	},
	methods: {
		async search() {
			const response = await axios.get(`/api/customers/?q=${this.searchInput}`);
			this.customers = response.data;
			this.reset = true;
		},
		async resetSearch() {
			const response = await axios.get('/api/customers/');
			this.customers = response.data;
			this.reset = false;
		},
		async deleteCustomer(id) {
			if (confirm('Are you sure you want to delete this customer?')) {
				const response = await axios.delete(`/api/customers/${id}`);
				this.customers = this.customers.filter(
					(customer) => customer.id !== id
				);
			}
		},
		addCustomer() {
			this.$router.push('/addcustomer');
		},
		async deleteService(id) {
			if (confirm('Are you sure you want to delete this service')) {
				const response = await axios.delete(`/api/services/${id}`);
				this.services = this.services.filter((service) => service.id !== id);

				const responseCustomers = await axios.get('/api/customers/');
				this.customers = responseCustomers.data;
			}
		},
		addService() {
			this.$router.push('/addservice');
		},
		editCustomer(id) {
			this.$router.push(`/editcustomer/${id}`);
		},
	},
};
</script>

<style scoped>
.table {
	background-color: white;
}
.action {
	width: 70px;
}
</style>
