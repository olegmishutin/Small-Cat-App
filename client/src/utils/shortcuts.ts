export function hideError(ids: string[]) {
  ids.forEach((value: string) => {
    const element = document.getElementById(`${value}_error`) as HTMLInputElement;
    if (element) {
      element.textContent = ''
    }
  })
}

export function showErrorFromResponse(errors: Record<string, string[]>) {
  Object.keys(errors).forEach((key) => {
    const element = document.getElementById(`${key}_error`) as HTMLInputElement;

    if (element) {
      element.textContent = errors[key][0]
    }
  });
}

export function showDetailErrorFromResponse(error: Record<string, string>, htmlElementIds: string) {
  if ('detail' in error) {
    const element = document.getElementById(htmlElementIds) as HTMLInputElement;
    element.textContent = error['detail']
  }
}
