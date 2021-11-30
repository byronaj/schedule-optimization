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
				newDate: null,
				myCal: null
			}
		},
		mounted() {
			this.myCal = new MiniCal({
				id: '#myCal',
				calendarSize: 'small',
				/*disableDayClick: "true",*/
				theme: 'glass',
				primaryColor: '#511b1b',
				dateChanged: this.dateChanged,
			});
			this.jump(new Date(new Date().setDate(new Date().getDate() + 7)))
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
			},
			jump(date) {
				setTimeout(() => { this.myCal.setDate(date); }, 500); 
			}
		},
	};
</script>

<style>
#myCal {
	text-align: center;
}
</style>