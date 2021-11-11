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
            <input type="number" style="width:45px;" max="12" min="1" value="8" ref="shifthours">
            Maximum hour shifts
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" value="5" ref="maxwork">
            Maximum consecutive working days
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" value="2" ref="minwork">
            Minimum consecutive working days
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" value="2" ref="minfree">
            Minimum consecutive free days
        </label>
        </div>
        
        <div class="field">
        <label class="checkbox">
            <input type="number" style="width:45px;" max="7" min="1" value="2" ref="maxweekend">
            Maximum consecutive weekends
        </label>
        </div>

        <div class="field">
        <label class="checkbox">
            <input type="checkbox" ref="back2back">
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
import Modal from "@/components/Modal.vue";

export default {
  components: { Modal },
  name: 'EditConstraints',
  data() {
		return {
			constraints: []
		};
	},
  methods: {
      toggleShowModal() {
          this.$parent.toggleEditConstraints()
      },
      saveConstraints() {
        this.constraints.push(["Max hour shifts", this.$refs.shifthours.value])
        this.constraints.push(["Max consecutive working days", this.$refs.maxwork.value])
        this.constraints.push(["Min consecutive working days", this.$refs.minwork.value])
        this.constraints.push(["Min consecutive free days", this.$refs.minfree.value])
        this.constraints.push(["Max consecutive weekends", this.$refs.maxweekend.value])
        this.constraints.push(["Back-to-Back Shifts", this.$refs.back2back.checked])
        //save constraints
      },
      getConstraints() {
          return this.constraints
      }
  }
}
</script>

<style>

</style>