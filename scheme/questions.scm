(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (if (null? s)
    (list )
    (begin 
      (define (helper l n)
        (if (null? (cdr l))
          (list (list n (car l)))
          (append (list (list n (car l))) (helper (cdr l) (+ n 1)))
        )
      )
      (helper s 0) 
    )
  )
)

  ; END PROBLEM 15

;; Problem 16

;; Merge two lists S1 and S2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  (cond 
    ((and (null? s1) (null? s2)) (list ))
    ((and (null? s1) (not (null? s2))) s2)
    ((and (not (null? s1)) (null? s2)) s1)
    (else 
      (cond 
          ((ordered? (car s1) (car s2)) (append (list (car s1)) (list (car s2)) (merge ordered? (cdr s1) (cdr s2))))
          ((ordered? (car s2) (car s1)) (append (list (car s2)) (list (car s1)) (merge ordered? (cdr s1) (cdr s2))))
          (else (merge ordered? (cdr s1) (cdr s2)))
      )  
    )
  )   
)
  ; END PROBLEM 16

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           'replace-this-line
           ; END OPTIONAL PROBLEM 2
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           'replace-this-line
           ; END OPTIONAL PROBLEM 2
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  'replace-this-line)
