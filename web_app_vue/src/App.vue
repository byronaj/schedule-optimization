<template>
	<div id="app">

		<Nav />

		<router-view />

		<font-awesome-icon icon="user-secret" />

	</div>
</template>

<script>
	import axios from 'axios';

	import Nav from '@/components/layout/Nav';

	export default {
		name: 'App',
		components: {
			Nav,
		},
		mounted() {
			document.title = 'Schedule Optimizer';
		},
		beforeCreate() {
			this.$store.commit('initializeStore');

			const token = this.$store.state.user.token;

			if (token) {
				axios.defaults.headers.common['Authorization'] = 'Token ' + token;
			} else {
				axios.defaults.headers.common['Authorization'] = '';
			}
		},
	};
</script>

<style lang="scss">
	@import '../node_modules/bulma';
</style>
