<script>
	import '@fullcalendar/core/vdom'; // solves problem with Vite
	import FullCalendar from '@fullcalendar/vue3';
	import resourceTimelinePlugin from '@fullcalendar/resource-timeline';
	import dayGridPlugin from '@fullcalendar/daygrid';
	import interactionPlugin from '@fullcalendar/interaction';
	import adaptivePlugin from '@fullcalendar/adaptive';

	import axios from 'axios';

	export default {
		components: {
			FullCalendar, // make the <FullCalendar> tag available
		},
		data() {
			return {
				calendarOptions: {
					plugins: [resourceTimelinePlugin, dayGridPlugin, interactionPlugin, adaptivePlugin],
					initialView: 'resourceTimelineDay',
					schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
					dateClick: this.handleDateClick,
					height: '88vh',
					titleFormat: {
						// will produce something like "Tuesday, September 18, 2018"
						month: 'long',
						year: 'numeric',
						day: 'numeric',
						weekday: 'long',
					},
					editable: false,
					headerToolbar: {
						left: 'title',
						right: '',
					},
					resourceAreaColumns: [
						{
							field: 'name',
							headerContent: 'Employees',
						},
					],
					resourceAreaWidth: '20%',
					eventResize: function (info) {
						alert(info.event.title + ' end is now ' + info.event.end.toISOString());

						if (!confirm('is this okay?')) {
							info.revert();
						}
					},
				},
				employee_fte: [],
			};
		},
		mounted() {
			this.getEmployees();
			this.getSchedule();
		},
		methods: {
			currentDate() {
				let date_ob = new Date();
				let date = ('0' + date_ob.getDate()).slice(-2);
				let month = ('0' + (date_ob.getMonth() + 1)).slice(-2);
				let year = date_ob.getFullYear();
				let current = year + '-' + month + '-' + date;
				//was using 'let current = new Date().toISOString().split('T')[0]'
				//but this was causing some issue with last 4 hours showing as next day
				return current;
			},
			handleDateClick: function (arg) {
				console.log('date click! ' + arg.dateStr);
			},
			changeDate(date) {
				let cal = this.$refs.FC.getApi();
				cal.gotoDate(date);
			},
			getDate() {
				let cal = this.$refs.FC.getApi();
				return cal.getDate();
			},
			getTestTime(shift, fte) {
				let time = ['', ''];
				if (shift == 0) {
					shift = Math.floor(Math.random() * 3) + 1;
				}
				switch (shift) {
					case 1:
						let st = Math.floor(Math.random() * 9) + 1; //shift starts between 1 and 9am
						let en = Math.round(st + 8 * parseFloat(fte)); //shift ends after 8*fte hours
						time[0] = st + ':00:00';
						time[1] = en + ':00:00';
						if (st < 10) {
							time[0] = '0' + time[0];
						}
						if (en < 10) {
							time[1] = '0' + time[1];
						}
						break;
					case 2:
						st = Math.floor(Math.random() * 6) + 9; //shift starts between 9am and 15 (3pm)
						en = Math.round(st + 8 * parseFloat(fte));
						time[0] = st + ':00:00';
						time[1] = en + ':00:00';
						if (st < 10) {
							time[0] = '0' + time[0];
						}
						break;
					case 3:
						st = Math.floor(Math.random() * 4) + 16; //shift starts between 16 (4pm) and 20 (8pm)
						en = Math.round(st + 8 * parseFloat(fte));
						if (en >= 24) {en -= 24} //if over 24 hours, subtract 24 to go into the next day
						time[0] = st + ':00:00';
						time[1] = en + ':00:00';
						if (en < 10) {
							time[1] = '0' + time[1];
						}
						break;
				}
				return time;
			},
			getEmployees() {
				axios
					.get(`/api/v1/employees/`)
					.then((response) => {
						//refresh resources resources
						let cal = this.$refs.FC.getApi();
						let tr = cal.getResources();
						for (let i = 0; i < tr.length; i++) {
							let res = cal.getResourceById(tr[i].id);
							res.remove();
						}
						for (let i = 0; i < response.data.length; i++) { //employees start with ID 1
							//create resource object
							let res = {
								id: response.data[i].id.toString().padStart(2, '0'), //so that they're in order
								name: response.data[i].first_name + ' ' + response.data[i].last_name,
							};
							this.employee_fte.push(response.data[i].fte)
							cal.addResource(res);
						}
					})
					.catch((error) => {
						console.log(error);
					});
			},
			getSchedule() {
				axios
					.get(`/api/v1/schedulesolver/`)
					.then((response) => {
						let cal = this.$refs.FC.getApi();
						let res = cal.getResources()
						let evTit = ['', 'First', 'Second', 'Third'];
						let evCol = ['', '#740008', '#705000', '#023e1c'];
						for (let i = 0; i < response.data.length; i++) { //for each employee
							for (let j = 0; j < response.data[i].shift_assignments.length; j++) { //for each shift assignment
								if (response.data[i].shift_assignments[j].assignment != 0) //working (0 == off)
								{
									let ttime = this.getTestTime(response.data[i].shift_assignments[j].assignment, this.employee_fte[i]);
									let end = response.data[i].shift_assignments[j].shift_date + 'T' + ttime[1]

									if ((""+ttime[1])[0] == "0" && response.data[i].shift_assignments[j].assignment == 3) { //if the ending of a 3rd shift
										let d = new Date(response.data[i].shift_assignments[j].shift_date);
										d.setDate(d.getDate() + 1); //move date to the next day
										end = d.toISOString().split('T')[0]  + 'T' + ttime[1];
									}

									let ev = {
										id: res[i].id + "-" + j,
										resourceId: res[i].id,
										title: evTit[response.data[i].shift_assignments[j].assignment] + ' Shift',
										extendedProps: { name: cal.getResourceById((i + 1).toString().padStart(2, '0')).extendedProps.name }, //name of employee for export
										start: response.data[i].shift_assignments[j].shift_date + 'T' + ttime[0],
										end: end,
										borderColor: '#000',
										backgroundColor: evCol[response.data[i].shift_assignments[j].assignment],
									};
									cal.addEvent(ev);
								}
							}
						}
					})
					.catch((error) => {
						console.log(error);
					});
			},
			getEvents() {
				let cal = this.$refs.FC.getApi();
				let ev = cal.getEvents()
				return ev
			}
		},
	};
</script>

<template>
	<FullCalendar :options="calendarOptions" ref="FC" />
</template>
