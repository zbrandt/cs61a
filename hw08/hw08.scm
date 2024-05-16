(define (ascending? s) 
    (cond ((null? s) #t) ((null? (cdr s)) #t) (else 
            (if (> (car s) (car (cdr s)) )
                #f
                (ascending? (cdr s))
            )
        )
    )
)

(define (my-filter pred s) 
    (if (null? s)
        (list )
        (if (pred (car s))
            (append (list (car s)) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
        )
    )
)

(define (interleave lst1 lst2) 
    (cond 
        ((and (null? lst1) (not (null? lst2))) lst2)
        ((and (null? lst2) (not (null? lst1))) lst1)
        ((and (null? lst1) (null? lst2)) (list))
        (else (append (list (car lst1)) (interleave lst2 (cdr lst1))))
    )
)

(define (no-repeats s) 
    (if (null? s)
        (list )
        (let (
            (x (append (list (car s)) (my-filter (lambda (x) (not (= x (car s)))) (cdr s))))
            )
        (append (list (car x)) (no-repeats (cdr x))) 
        )
    )
)
