<template>
	<div id="myCal"></div>
</template>

<script>
	import MiniCal from 'color-calendar';
	import 'color-calendar/dist/css/theme-glass.css';

	export default {
		name: 'ColorCalendar',
		data() {
			return {
				newDate: null
			}
		},
		mounted() {
			new MiniCal({
				id: '#myCal',
				calendarSize: 'small',
				/*disableDayClick: "true",*/
				theme: 'glass',
				primaryColor: '#511b1b',
				dateChanged: this.dateChanged,
			});
		},
		methods: {
			dateChanged(date) {
				try {
					this.newDate = date;
					this.$parent.$refs.FullCalendar.changeDate(date);
				} catch {}
			},
			getDate() {
				return this.newDate;
			}
		},
	};
</script>

<style>
#myCal {
	text-align: center;
}
</style>