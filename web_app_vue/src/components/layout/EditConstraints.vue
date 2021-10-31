<template>
  <Modal @close="toggleShowModal">
    <header class="modal-card-head">
        <p class="modal-card-title">
        Edit Constraints
        </p>
        <button class="delete" aria-label="close" @click="toggleShowModal"></button>
    </header>

    <section class="modal-card-body" style="color:black;">
        <div class="field">
        <label class="checkbox">
            <input type="checkbox" ref="shift12hours">
            Shifts no more than 12 hours
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
      showModal: false,
    }
  },
  methods: {
      toggleShowModal() {
          this.$parent.toggleEditConstraints()
      },
      saveConstraints() {
        let shift12hours = this.$refs.shift12hours.checked
        let back2back = this.$refs.back2back.checked
        //save constraints
      }
  }
}
</script>

<style>

</style>