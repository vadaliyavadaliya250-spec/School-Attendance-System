// Highlight today's date input
document.addEventListener('DOMContentLoaded', () => {
  const di = document.getElementById('dateInput');
  if (di) {
    const today = new Date().toISOString().split('T')[0];
    if (di.value === today) {
      di.classList.add('border-primary');
    }
  }
});
