import tkinter as tk
from tkinter import messagebox

# ── Ventana principal ──────────────────────────────────────────────────────────
ventana = tk.Tk()
ventana.title("Ejercicios de Programacion")
ventana.geometry("400x500")
ventana.config(bg="#f0f0f0")

tk.Label(ventana, text="Ejercicios de Programacion",
         font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

tk.Label(ventana, text="Elige un ejercicio:",
         font=("Arial", 12), bg="#f0f0f0").pack()


# ── Funcion para abrir una ventana nueva ──────────────────────────────────────
def abrir_ventana(titulo, construir_ejercicio):
    nueva = tk.Toplevel(ventana)
    nueva.title(titulo)
    nueva.geometry("500x550")
    nueva.config(bg="#f0f0f0")
    tk.Label(nueva, text=titulo, font=("Arial", 14, "bold"),
             bg="#4a90d9", fg="white", pady=10).pack(fill="x")
    construir_ejercicio(nueva)


# ── Caja de texto con scroll ───────────────────────────────────────────────────
def crear_resultado(ventana_padre):
    marco = tk.Frame(ventana_padre, bg="#f0f0f0")
    marco.pack(fill="both", expand=True, padx=10, pady=10)
    scroll = tk.Scrollbar(marco)
    scroll.pack(side="right", fill="y")
    caja = tk.Text(marco, height=10, font=("Courier", 10),
                   bg="white", fg="#222", state="disabled",
                   yscrollcommand=scroll.set)
    caja.pack(side="left", fill="both", expand=True)
    scroll.config(command=caja.yview)
    return caja


def mostrar(caja, texto):
    caja.config(state="normal")
    caja.insert("end", texto + "\n")
    caja.see("end")
    caja.config(state="disabled")


def limpiar(caja):
    caja.config(state="normal")
    caja.delete("1.0", "end")
    caja.config(state="disabled")


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 1 - Aumento de sueldos
# ══════════════════════════════════════════════════════════════════════════════
def ej1(padre):
    historial = []

    tk.Label(padre, text="Nombre:", bg="#f0f0f0").pack()
    entry_nombre = tk.Entry(padre, font=("Arial", 11)); entry_nombre.pack(fill="x", padx=20)

    tk.Label(padre, text="Sueldo basico:", bg="#f0f0f0").pack()
    entry_sueldo = tk.Entry(padre, font=("Arial", 11)); entry_sueldo.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def calcular():
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Ingresa el nombre."); return
        try:
            sueldo = float(entry_sueldo.get())
        except ValueError:
            messagebox.showerror("Error", "Sueldo invalido."); return

        if sueldo < 4000:
            porcentaje = 0.15
        elif sueldo <= 7000:
            porcentaje = 0.10
        else:
            porcentaje = 0.08

        aumento = sueldo * porcentaje
        nuevo_sueldo = sueldo + aumento
        historial.append((nombre, sueldo, aumento, nuevo_sueldo))

        limpiar(resultado)
        mostrar(resultado, f"Nombre  : {nombre}")
        mostrar(resultado, f"Sueldo  : S/ {sueldo:.2f}")
        mostrar(resultado, f"Aumento : {porcentaje*100:.0f}%  ->  S/ {aumento:.2f}")
        mostrar(resultado, f"Nuevo   : S/ {nuevo_sueldo:.2f}")
        entry_nombre.delete(0, "end")
        entry_sueldo.delete(0, "end")

    def ver_historial():
        if not historial:
            messagebox.showinfo("Historial", "No hay registros."); return
        limpiar(resultado)
        mostrar(resultado, f"=== Historial ({len(historial)} trabajadores) ===")
        for i, (n, s, a, nu) in enumerate(historial, 1):
            mostrar(resultado, f"{i}. {n}  S/{s:.2f} -> S/{nu:.2f}  (+{(a/s*100):.0f}%)")

    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Registrar", command=calcular,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Ver historial", command=ver_historial,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 2 - Parque de diversiones
# ══════════════════════════════════════════════════════════════════════════════
def ej2(padre):
    visitantes = []

    tk.Label(padre, text="Nombre:", bg="#f0f0f0").pack()
    entry_nombre = tk.Entry(padre, font=("Arial", 11)); entry_nombre.pack(fill="x", padx=20)

    tk.Label(padre, text="Edad:", bg="#f0f0f0").pack()
    entry_edad = tk.Entry(padre, font=("Arial", 11)); entry_edad.pack(fill="x", padx=20)

    tk.Label(padre, text="Numero de juegos:", bg="#f0f0f0").pack()
    entry_juegos = tk.Entry(padre, font=("Arial", 11)); entry_juegos.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def registrar():
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Ingresa el nombre."); return
        try:
            edad   = int(entry_edad.get())
            juegos = int(entry_juegos.get())
        except ValueError:
            messagebox.showerror("Error", "Datos invalidos."); return

        total_base = juegos * 50

        if edad < 10:
            descuento = 0.25
        elif edad <= 17:
            descuento = 0.10
        else:
            descuento = 0.0

        monto_descuento = total_base * descuento
        total_pago = total_base - monto_descuento
        visitantes.append((nombre, edad, juegos, total_pago))

        limpiar(resultado)
        mostrar(resultado, f"Nombre   : {nombre}  (edad {edad})")
        mostrar(resultado, f"Juegos   : {juegos} x S/50 = S/{total_base:.2f}")
        mostrar(resultado, f"Descuento: {descuento*100:.0f}%  ->  -S/{monto_descuento:.2f}")
        mostrar(resultado, f"TOTAL    : S/{total_pago:.2f}")
        entry_nombre.delete(0, "end")
        entry_edad.delete(0, "end")
        entry_juegos.delete(0, "end")

    def ver_total():
        if not visitantes:
            messagebox.showinfo("Info", "Sin visitantes."); return
        limpiar(resultado)
        mostrar(resultado, f"=== Reporte ({len(visitantes)} visitantes) ===")
        for i, (n, e, j, t) in enumerate(visitantes, 1):
            mostrar(resultado, f"{i}. {n} (edad:{e})  {j} juegos  -> S/{t:.2f}")
        mostrar(resultado, f"TOTAL RECAUDADO: S/{sum(v[3] for v in visitantes):.2f}")

    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Registrar", command=registrar,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Total recaudado", command=ver_total,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 3 - Descuentos por mes
# ══════════════════════════════════════════════════════════════════════════════
def ej3(padre):
    compras = []

    DESCUENTOS = {
        "octubre":   0.15,
        "diciembre": 0.20,
        "julio":     0.10,
    }

    tk.Label(padre, text="Nombre del cliente:", bg="#f0f0f0").pack()
    entry_nombre = tk.Entry(padre, font=("Arial", 11)); entry_nombre.pack(fill="x", padx=20)

    tk.Label(padre, text="Mes de la compra (ej: julio):", bg="#f0f0f0").pack()
    entry_mes = tk.Entry(padre, font=("Arial", 11)); entry_mes.pack(fill="x", padx=20)

    tk.Label(padre, text="Importe:", bg="#f0f0f0").pack()
    entry_importe = tk.Entry(padre, font=("Arial", 11)); entry_importe.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def registrar():
        nombre  = entry_nombre.get().strip()
        mes     = entry_mes.get().strip().lower()
        if not nombre:
            messagebox.showwarning("Aviso", "Ingresa el nombre."); return
        try:
            importe = float(entry_importe.get())
        except ValueError:
            messagebox.showerror("Error", "Importe invalido."); return

        porcentaje = DESCUENTOS.get(mes, 0.0)
        monto_desc = importe * porcentaje
        total      = importe - monto_desc
        compras.append((nombre, mes, importe, total))

        limpiar(resultado)
        mostrar(resultado, f"Cliente  : {nombre}")
        mostrar(resultado, f"Mes      : {mes.capitalize()}")
        mostrar(resultado, f"Importe  : S/{importe:.2f}")
        mostrar(resultado, f"Descuento: {porcentaje*100:.0f}%  (-S/{monto_desc:.2f})")
        mostrar(resultado, f"TOTAL    : S/{total:.2f}")
        entry_nombre.delete(0, "end")
        entry_mes.delete(0, "end")
        entry_importe.delete(0, "end")

    def ver_total():
        if not compras:
            messagebox.showinfo("Info", "Sin compras."); return
        limpiar(resultado)
        mostrar(resultado, f"=== Ventas del dia ({len(compras)} compras) ===")
        for i, (n, m, imp, tot) in enumerate(compras, 1):
            mostrar(resultado, f"{i}. {n} ({m.capitalize()})  S/{imp:.2f} -> S/{tot:.2f}")
        mostrar(resultado, f"TOTAL VENDIDO: S/{sum(c[3] for c in compras):.2f}")

    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Registrar", command=registrar,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Total del dia", command=ver_total,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 4 - Validar numero menor que 10
# ══════════════════════════════════════════════════════════════════════════════
def ej4(padre):
    intentos = [0]

    tk.Label(padre, text="Ingresa un numero menor que 10:", bg="#f0f0f0",
             font=("Arial", 11)).pack(pady=10)
    entry_num = tk.Entry(padre, font=("Arial", 14)); entry_num.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def validar():
        try:
            numero = int(entry_num.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa un numero entero."); return

        intentos[0] += 1

        if numero < 10:
            limpiar(resultado)
            mostrar(resultado, "Numero valido!")
            mostrar(resultado, f"Numero ingresado   : {numero}")
            mostrar(resultado, f"Intentos realizados: {intentos[0]}")
            intentos[0] = 0
        else:
            mostrar(resultado, f"Intento {intentos[0]}: {numero} no es menor que 10.")

        entry_num.delete(0, "end")

    entry_num.bind("<Return>", lambda e: validar())
    tk.Button(padre, text="Validar", command=validar,
              bg="#4a90d9", fg="white", font=("Arial", 12)).pack(pady=8)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 5 - Validar rango (0, 20)
# ══════════════════════════════════════════════════════════════════════════════
def ej5(padre):
    intentos = [0]

    tk.Label(padre, text="Ingresa un numero entre 1 y 19:", bg="#f0f0f0",
             font=("Arial", 11)).pack(pady=10)
    entry_num = tk.Entry(padre, font=("Arial", 14)); entry_num.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def validar():
        try:
            numero = int(entry_num.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa un numero entero."); return

        intentos[0] += 1

        if 0 < numero < 20:
            limpiar(resultado)
            mostrar(resultado, "Numero dentro del rango!")
            mostrar(resultado, f"Numero  : {numero}")
            mostrar(resultado, f"Intentos: {intentos[0]}")
            intentos[0] = 0
        elif numero <= 0:
            mostrar(resultado, f"Intento {intentos[0]}: {numero} es muy bajo (minimo 1).")
        else:
            mostrar(resultado, f"Intento {intentos[0]}: {numero} es muy alto (maximo 19).")

        entry_num.delete(0, "end")

    entry_num.bind("<Return>", lambda e: validar())
    tk.Button(padre, text="Validar", command=validar,
              bg="#4a90d9", fg="white", font=("Arial", 12)).pack(pady=8)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 6 - Registro de intentos
# ══════════════════════════════════════════════════════════════════════════════
def ej6(padre):
    historial = []
    incorrectos = [0]

    tk.Label(padre, text="Ingresa un numero entre 1 y 19:", bg="#f0f0f0",
             font=("Arial", 11)).pack(pady=10)
    entry_num = tk.Entry(padre, font=("Arial", 14)); entry_num.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def validar():
        try:
            numero = int(entry_num.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa un numero entero."); return

        historial.append(numero)
        en_rango = 0 < numero < 20

        if en_rango:
            limpiar(resultado)
            mostrar(resultado, f"Numero valido -> {numero}")
            mostrar(resultado, f"Todos los intentos  : {historial}")
            mostrar(resultado, f"Intentos incorrectos: {incorrectos[0]}")
            mostrar(resultado, f"Total de intentos   : {len(historial)}")
            incorrectos[0] = 0
        else:
            incorrectos[0] += 1
            mostrar(resultado, f"#{len(historial)}: {numero} fuera de rango -> historial: {historial}")

        entry_num.delete(0, "end")

    def ver_historial():
        if not historial:
            messagebox.showinfo("Historial", "No hay intentos."); return
        limpiar(resultado)
        mostrar(resultado, "=== Historial de intentos ===")
        for i, n in enumerate(historial, 1):
            estado = "OK" if 0 < n < 20 else "FUERA"
            mostrar(resultado, f"  {i}. {n}  [{estado}]")
        mostrar(resultado, f"Incorrectos: {incorrectos[0]}  |  Total: {len(historial)}")

    entry_num.bind("<Return>", lambda e: validar())
    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Validar", command=validar,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Ver historial", command=ver_historial,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 7 - Suma de los primeros N numeros
# ══════════════════════════════════════════════════════════════════════════════
def ej7(padre):
    tk.Label(padre, text="Ingresa N (entero positivo):", bg="#f0f0f0",
             font=("Arial", 11)).pack(pady=10)
    entry_n = tk.Entry(padre, font=("Arial", 14)); entry_n.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def calcular():
        try:
            n = int(entry_n.get())
            if n <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa un entero positivo."); return

        total = n * (n + 1) // 2

        limpiar(resultado)
        mostrar(resultado, f"Suma de los primeros {n} numeros:")
        mostrar(resultado, f"Formula: n x (n+1) / 2")
        mostrar(resultado, f"        {n} x {n+1} / 2 = {total}")

    entry_n.bind("<Return>", lambda e: calcular())
    tk.Button(padre, text="Calcular", command=calcular,
              bg="#4a90d9", fg="white", font=("Arial", 12)).pack(pady=8)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 8 - Suma acumulativa
# ══════════════════════════════════════════════════════════════════════════════
def ej8(padre):
    numeros  = []
    suma     = [0]

    tk.Label(padre, text="Ingresa numeros uno a uno (0 = terminar):",
             bg="#f0f0f0", font=("Arial", 11)).pack(pady=10)
    entry_num = tk.Entry(padre, font=("Arial", 14)); entry_num.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)
    mostrar(resultado, "Empieza a ingresar numeros:")

    def agregar():
        try:
            numero = float(entry_num.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa un numero valido."); return

        if numero == 0:
            finalizar()
            return

        numeros.append(numero)
        suma[0] += numero
        mostrar(resultado, f"  #{len(numeros):>2}  Numero: {numero:>10.2f}  |  Acumulado: {suma[0]:>12.2f}")
        entry_num.delete(0, "end")

    def finalizar():
        if not numeros:
            messagebox.showinfo("Info", "No se ingresaron numeros."); return
        mostrar(resultado, "-" * 46)
        mostrar(resultado, f"Cantidad  : {len(numeros)}")
        mostrar(resultado, f"SUMA TOTAL: {suma[0]:.2f}")
        numeros.clear(); suma[0] = 0
        entry_num.delete(0, "end")

    def reiniciar():
        numeros.clear(); suma[0] = 0
        limpiar(resultado)
        mostrar(resultado, "Reiniciado. Empieza de nuevo:")
        entry_num.delete(0, "end")

    entry_num.bind("<Return>", lambda e: agregar())
    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Agregar", command=agregar,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Finalizar (0)", command=finalizar,
              bg="#e07050", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Reiniciar", command=reiniciar,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 9 - Suma hasta superar 100
# ══════════════════════════════════════════════════════════════════════════════
def ej9(padre):
    numeros = []
    suma    = [0]
    activo  = [True]
    LIMITE  = 100

    tk.Label(padre, text=f"La suma para cuando supere {LIMITE}:",
             bg="#f0f0f0", font=("Arial", 11)).pack(pady=10)
    entry_num = tk.Entry(padre, font=("Arial", 14)); entry_num.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)
    mostrar(resultado, f"Ingresa numeros (se detiene al pasar {LIMITE}):")

    def agregar():
        if not activo[0]:
            messagebox.showinfo("Info", f"La suma ya supero {LIMITE}. Reinicia."); return
        try:
            numero = int(entry_num.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa un entero."); return

        numeros.append(numero)
        suma[0] += numero
        mostrar(resultado, f"  #{len(numeros):>2}  Numero: {numero:>8}  |  Suma: {suma[0]:>6}")
        entry_num.delete(0, "end")

        if suma[0] > LIMITE:
            activo[0] = False
            mostrar(resultado, "-" * 44)
            mostrar(resultado, f"La suma supero {LIMITE}!")
            mostrar(resultado, f"Numeros  : {numeros}")
            mostrar(resultado, f"Cantidad : {len(numeros)}")
            mostrar(resultado, f"SUMA FINAL: {suma[0]}")

    def reiniciar():
        numeros.clear(); suma[0] = 0; activo[0] = True
        limpiar(resultado)
        mostrar(resultado, f"Reiniciado. Ingresa numeros (limite {LIMITE}):")
        entry_num.delete(0, "end")

    entry_num.bind("<Return>", lambda e: agregar())
    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Agregar", command=agregar,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Reiniciar", command=reiniciar,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ══════════════════════════════════════════════════════════════════════════════
# EJERCICIO 10 - Pago de trabajadores
# ══════════════════════════════════════════════════════════════════════════════
def ej10(padre):
    trabajadores = []

    tk.Label(padre, text="Nombre:", bg="#f0f0f0").pack()
    entry_nombre = tk.Entry(padre, font=("Arial", 11)); entry_nombre.pack(fill="x", padx=20)

    tk.Label(padre, text="Horas normales:", bg="#f0f0f0").pack()
    entry_hnorm = tk.Entry(padre, font=("Arial", 11)); entry_hnorm.pack(fill="x", padx=20)

    tk.Label(padre, text="Pago por hora:", bg="#f0f0f0").pack()
    entry_pago = tk.Entry(padre, font=("Arial", 11)); entry_pago.pack(fill="x", padx=20)

    tk.Label(padre, text="Horas extras:", bg="#f0f0f0").pack()
    entry_hextra = tk.Entry(padre, font=("Arial", 11)); entry_hextra.pack(fill="x", padx=20)

    tk.Label(padre, text="Numero de hijos:", bg="#f0f0f0").pack()
    entry_hijos = tk.Entry(padre, font=("Arial", 11)); entry_hijos.pack(fill="x", padx=20)

    resultado = crear_resultado(padre)

    def calcular():
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Ingresa el nombre."); return
        try:
            h_norm  = float(entry_hnorm.get())
            pago_h  = float(entry_pago.get())
            h_extra = float(entry_hextra.get())
            hijos   = int(entry_hijos.get())
        except ValueError:
            messagebox.showerror("Error", "Revisa los valores numericos."); return

        pago_normal = h_norm * pago_h
        pago_extra  = h_extra * pago_h * 1.5
        bonif_hijos = hijos * 0.5 * pago_h
        total       = pago_normal + pago_extra + bonif_hijos

        trabajadores.append((nombre, total))

        limpiar(resultado)
        mostrar(resultado, f"Trabajador: {nombre}")
        mostrar(resultado, "-" * 40)
        mostrar(resultado, f"Hrs normales : {h_norm}h x S/{pago_h:.2f} = S/{pago_normal:.2f}")
        mostrar(resultado, f"Hrs extras   : {h_extra}h x S/{pago_h*1.5:.2f} = S/{pago_extra:.2f}")
        mostrar(resultado, f"Bonif. hijos : {hijos} hijo(s) -> S/{bonif_hijos:.2f}")
        mostrar(resultado, "-" * 40)
        mostrar(resultado, f"PAGO TOTAL   : S/{total:.2f}")
        for entry in [entry_nombre, entry_hnorm, entry_pago, entry_hextra, entry_hijos]:
            entry.delete(0, "end")

    def ver_reporte():
        if not trabajadores:
            messagebox.showinfo("Reporte", "Sin trabajadores."); return
        limpiar(resultado)
        mostrar(resultado, f"=== Reporte de pagos ({len(trabajadores)} trabajadores) ===")
        for i, (n, t) in enumerate(trabajadores, 1):
            mostrar(resultado, f"{i}. {n:<20}  S/{t:.2f}")
        mostrar(resultado, f"TOTAL EMPRESA: S/{sum(t for _, t in trabajadores):.2f}")

    marco_botones = tk.Frame(padre, bg="#f0f0f0"); marco_botones.pack(pady=5)
    tk.Button(marco_botones, text="Calcular", command=calcular,
              bg="#4a90d9", fg="white", font=("Arial", 11)).pack(side="left", padx=5)
    tk.Button(marco_botones, text="Ver reporte", command=ver_reporte,
              bg="#888", fg="white", font=("Arial", 11)).pack(side="left", padx=5)


# ── Lista de ejercicios y botones del menu ────────────────────────────────────
ejercicios = [
    ("01 - Aumento de sueldos",    ej1),
    ("02 - Parque de diversiones", ej2),
    ("03 - Descuentos por mes",    ej3),
    ("04 - Validar numero < 10",   ej4),
    ("05 - Validar rango (0,20)",  ej5),
    ("06 - Registro de intentos",  ej6),
    ("07 - Suma de N numeros",     ej7),
    ("08 - Suma acumulativa",      ej8),
    ("09 - Suma hasta limite 100", ej9),
    ("10 - Pago de trabajadores",  ej10),
]

marco_botones = tk.Frame(ventana, bg="#f0f0f0")
marco_botones.pack(pady=10)

for titulo, funcion in ejercicios:
    def abrir(t=titulo, f=funcion):
        abrir_ventana(t, f)

    tk.Button(marco_botones, text=titulo, command=abrir,
              bg="white", fg="#333", font=("Arial", 11),
              relief="solid", bd=1, padx=10, pady=4,
              cursor="hand2").pack(fill="x", pady=2, padx=20)

ventana.mainloop()
