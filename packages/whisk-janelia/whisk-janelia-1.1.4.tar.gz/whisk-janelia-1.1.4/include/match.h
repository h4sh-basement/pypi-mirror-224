/* Author: Nathan Clack <clackn@janelia.hhmi.org>
 * Date  : 2008 
 *
 * Copyright 2010 Howard Hughes Medical Institute.
 * All rights reserved.
 * Use is subject to Janelia Farm Research Campus Software Copyright 1.1
 * license terms (http://license.janelia.org/license/jfrc_copyright_1_1.html).
 */
/*
 *  match.h
 *  
 *  Adapted from Markus Buehren's implimentation of the Munkres (a.k.a. Hungarian)
 *  algorithm.
 *
 *  Adapted by Nathan Clack on 3/5/08.
 *  Copyright 2008 HHMI. All rights reserved.
 *
 */

#ifndef H_MATCH
#define H_MATCH

#include "compat.h"

typedef struct _Assignment
{ double  *assignment; 
  double  cost;
  int     n;
} Assignment;

SHARED_EXPORT Assignment match( double* distMatrixIn, int nOfRows, int nOfColumns );
SHARED_EXPORT void assignmentoptimal(double *assignment, double *cost, double *distMatrixIn, int nOfRows, int nOfColumns);

/* Matrix printing functions (for debuging mostly)*/
void pmat( double* array, int m, int n);
void pimat( int* array, int m, int n);
void pxmat(char* array, int m, int n);

#endif
