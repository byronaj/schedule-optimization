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
				isLoading: true,
			};
		},
		methods: {
			toggleShowExport() {
				this.$parent.exportCalendar();
			},
			setDate(date) {
				let cal = this.$refs.FC.getApi();
				cal.gotoDate(date);
			},
			setEvents(ev) {
				let cal = this.$refs.FC.getApi();
				var cd = cal.getDate();
				cd.setDate(cd.getDate() + (((1 + 6 - cd.getDay()) % 7) || 7)); //next Sunday

				let i = 0;
				for (i = 0; i < ev.length; i++)
				{
					let d = new Date(ev[i].start)
					if (d.getTime() < cd.getTime()) //to limit the time it takes to generate
					{
						ev[i].setProp( 'title', ev[i].extendedProps.name )
						cal.addEvent(ev[i])
					}
				}
				setTimeout(() => { //because the FullCalendar doesn't open up fast enough
					try {
						this.isLoading = false;
						setTimeout(() => { window.print(); }, 100); //because the loader doesn't disappear fast enough
					}
					catch { }
				}, 1000);
			},
		},
	};
</script>
<template>
	<div id="export">
		<Modal @close="toggleShowExport">
			<section class="modal-card-body export" style="color: black">
				<div class="loader-wrapper" :class="{ 'is-active-loading': isLoading }">
					<div class="loader is-loading"></div>
				</div>
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
	.loader-wrapper {
		position: absolute;
		top: 0;
		left: 0;
		height: 100%;
		width: 100%;
		background: #fff;
		opacity: 0;
		z-index: -1;
		transition: opacity .3s;
		display: flex;
		justify-content: center;
		align-items: center;
		border-radius: 6px;
	}
	.loader {
		height: 80px;
		width: 80px;
	}
	.is-active-loading {
        opacity: 1;
        z-index: 2;
    }
</style>
