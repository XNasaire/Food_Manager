package com.foodmanager.repository;

import com.foodmanager.model.Plat;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PlatRepository extends JpaRepository<Plat, Long> {
    List<Plat> findByIdUtilisateur(Long idUtilisateur);
}