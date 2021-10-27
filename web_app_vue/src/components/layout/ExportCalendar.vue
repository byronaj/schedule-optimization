<script>
import '@fullcalendar/core/vdom' // solves problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import adaptivePlugin from '@fullcalendar/adaptive'

import Modal from "@/components/Modal.vue";

export default {
  components: {
    FullCalendar, // make the <FullCalendar> tag available
    Modal
  },
  data() {
    return {
      calendarOptions: {
        plugins: [ dayGridPlugin, adaptivePlugin ],
        initialView: 'dayGridMonth',
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        headerToolbar: {
          left: '',
          right: '',
        },
        resources: [
          {
            id: 'a',
            name: 'Employee Name',
            eventColor: '#511b1b',
            
          }
        ],
        events: [
          {
            id: '1',
            resourceId: 'a',
            title: 'Day Shift',
            start: this.currentDate() + 'T10:30:00',
            end: this.currentDate() + 'T20:30:00',
          }
        ],
      },
      showModal: false,
    }
  },
  methods: {
      toggleShowExport() {
          this.$parent.exportCalendar()
      },
      currentDate() {
        const current = new Date();
        var d = current.getFullYear() + '-' + (current.getMonth()+1) + '-' + current.getDate();
        return d;
    },
  }
}
</script>
<template>
  <Modal @close="toggleShowExport">
    <section class="modal-card-body" style="color:black; padding: 10px 50px;">
      <FullCalendar :options="calendarOptions" ref="FC"/>
      <button class="button" aria-label="close" @click="toggleShowExport">
        Close
      </button>
    </section>
  </Modal>
</template>

<style>
.modal-card {
  width: 100%;
  max-height: 90vh;
  /*height: 100%;*/
}
</style>