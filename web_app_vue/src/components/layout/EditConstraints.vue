<template>
  <Modal @close="toggleShowModal">
    <header class="modal-card-head">
        <p class="modal-card-title">
        Edit Global Constraints
        </p>
        <button class="delete" aria-label="close" @click="toggleShowModal"></button>
    </header>

    <section class="modal-card-body" style="color:black;">
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="12" min="1" v-model="shifthours">
            Maximum hour shifts
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" v-model="maxwork">
            Maximum consecutive working days
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" v-model="minwork">
            Minimum consecutive working days
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" v-model="minfree">
            Minimum consecutive free days
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" v-model="maxweekend">
            Maximum consecutive weekends
        </label>
        </div>

        <div class="field">
        <label class="checkbox">
            <input type="checkbox" v-model="back2back">
            Allow back-to-back shifts
        </label>
        </div>
    </section>
    <footer class="modal-card-foot">
        <button class="button is-success" @click="saveConstraints">
        Save changes
        </button>
        <button class="button" aria-label="close" @click="toggleShowModal">
        Cancel
        </button>
    </footer>

    </Modal>
</template>

<script>
import axios from "axios";

import Modal from "@/components/Modal.vue";

export default {
  components: { Modal },
  name: 'EditConstraints',
  data() {
      return {
            shifthours: 8,
            maxwork: 5,
            minwork: 2,
            minfree: 2,
            maxweekend: 2,
            back2back: true,
      }
  },
  methods: {
      toggleShowModal() {
          this.$parent.toggleEditConstraints()
      },
      saveConstraints() {
        this.$store.state.globalconstraints[0][1] = this.shifthours;
        this.$store.state.globalconstraints[1][1] = this.maxwork;
        this.$store.state.globalconstraints[2][1] = this.minwork;
        this.$store.state.globalconstraints[3][1] = this.minfree;
        this.$store.state.globalconstraints[4][1] = this.maxweekend;
        this.$store.state.globalconstraints[5][1] = this.back2back;
        this.toggleShowModal()
        //save constraints
      }
  },
  mounted() {
      //update constraints from storage
      this.shifthours = this.$store.state.globalconstraints[0][1];
      this.maxwork = this.$store.state.globalconstraints[1][1];
      this.minwork = this.$store.state.globalconstraints[2][1];
      this.minfree = this.$store.state.globalconstraints[3][1];
      this.maxweekend = this.$store.state.globalconstraints[4][1];
      this.back2back = this.$store.state.globalconstraints[5][1];
  }
}
</script>

<style>

</style>