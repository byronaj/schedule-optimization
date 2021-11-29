<script>
	import '@fullcalendar/core/vdom'; // solves problem with Vite
	import FullCalendar from '@fullcalendar/vue3';
	//import dayGridPlugin from '@fullcalendar/daygrid'
	import adaptivePlugin from '@fullcalendar/adaptive';
	import timeGridPlugin from '@fullcalendar/timegrid';

	import Modal from '@/components/Modal.vue';

	export default {
		components: {
			FullCalendar, // make the <FullCalendar> tag available
			Modal,
		},
		data() {
			return {
				calendarOptions: {
					plugins: [timeGridPlugin, adaptivePlugin],
					initialView: 'timeGridWeek',
					schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
					allDaySlot: false,
					slotDuration: '01:00:00',
					height: '73vh',
					headerToolbar: {
						left: 'title',
						right: '',
					},
					titleFormat: {
						// will produce something like "Tuesday, September 18, 2018"
						month: 'long',
						year: 'numeric',
						day: 'numeric',
						weekday: 'long',
					},
				},
				showModal: false,
			};
		},
		methods: {
			toggleShowExport() {
				this.$parent.exportCalendar();
			},
			setEvents(ev) {
				let cal = this.$refs.FC.getApi();
				var cd = new Date();
				cd.setDate(cd.getDate() + (((1 + 6 - cd.getDay()) % 7) || 7)); //next Sunday
				for (let i = 0; i < ev.length; i++)
				{
					let d = new Date(ev[i].start)
					if (d.getTime() < cd.getTime()) //to limit the time it takes to generate
					{
						ev[i].setProp( 'title', ev[i].extendedProps.name )
						cal.addEvent(ev[i])
					}
				}
				window.print();
			}
		},
	};
</script>
<template>
	<div id="export">
		<Modal @close="toggleShowExport">
			<section class="modal-card-body export" style="color: black">
				<FullCalendar :options="calendarOptions" ref="FC" />
				<button class="button is-hidden-print" aria-label="close" @click="toggleShowExport">Close</button>
			</section>
		</Modal>
	</div>
	>
</template>

<style>
	#export .modal-card {
		width: 100%;
	}
	@media print {
		.is-hidden-print {
			display: none !important;
		}
	}
</style>
